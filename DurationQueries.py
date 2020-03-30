import googlemaps

from repository.Caching import write_cache
from repository.Database import *
from repository.DbOperations import address_exists


def save_address(address, name, lat, lng):
    if not address_exists(address):
        new_coordinates = LocationCoordinates(
            address=address,
            name=name,
            lat=lat,
            lng=lng)
        save_obj(new_coordinates)


def save_duration_results(origin_input, dest_input, query_name, results):
    results = DurationQueryResult(
        origin_name=origin_input,
        dest_name=dest_input,
        duration_sec=results['duration']['value'],
        duration_min=results['duration']['text'],
        distance_m=results['distance']['value'],
        distance_mi=results['distance']['text'],
        traffic_duration_sec=results['duration_in_traffic']['value'],
        traffic_duration_min=results['duration_in_traffic']['text'],
        query_name=query_name)
    save_obj(results)


def store_results(query_name, origin_input, dest_input, directions_result):
    results = directions_result[0]['legs'][0]

    dist_mi = results['distance']['text']
    duration_min = results['duration']['text']
    duration_traffic_min = results['duration_in_traffic']['text']

    origin_address = results['start_address']
    dest_address = results['end_address']

    origin_lat = results['start_location']['lat']
    origin_lng = results['start_location']['lng']

    dest_lat = results['end_location']['lat']
    dest_lng = results['end_location']['lng']

    save_address(origin_address, origin_input, origin_lat, origin_lng)
    save_address(dest_address, dest_input, dest_lat, dest_lng)
    save_duration_results(origin_input, dest_input, query_name, results)

    output = """
    Start: {} ({})
    End: {} ({})

    Distance: {}
    Duration: {}
    With Traffic: {}

    """.format(
        origin_input, origin_address,
        dest_input, dest_address,
        dist_mi,
        duration_min,
        duration_traffic_min)

    print(output)


def query_trip_data(name, origin, dest, client):
    now = datetime.now()
    print(str(now))
    save_obj(ApiAccessEvent())
    #todo Fix to actually use mode from db table (right now hardcoded to 'driving'
    directions_result = client.directions(origin,
                                          dest,
                                          mode="driving",
                                          departure_time=now)
    # write_cache('{}_{}.txt'.format(name, str(now)), directions_result)
    store_results(name, origin, dest, directions_result)
    return directions_result


def fetch_client(key):
    print('Fetching maps client')
    return googlemaps.Client(key)


def fetch_api_key():
    print('Fetching api key...')
    with open("maps.key", 'r') as f:
        return f.readline()
