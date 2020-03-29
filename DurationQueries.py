import googlemaps

from Caching import write_cache
from repository.Database import *


def store_results(start, end, directions_result):
    results = directions_result[0]['legs'][0]

    dist_m = results['distance']['value']
    dist_mi = results['distance']['text']
    duration_sec = results['duration']['value']
    duration_min = results['duration']['text']
    duration_traffic_min = results['duration_in_traffic']['text']
    duration_traffic_sec = results['duration_in_traffic']['value']

    end_address = results['end_address']
    start_address = results['start_address']

    start_lat = results['start_location']['lat']
    start_lng = results['start_location']['lng']

    end_lat = results['end_location']['lat']
    end_lng = results['end_location']['lng']



    output = """
    Start: {} ({})
    End: {} ({})

    Distance: {}
    Duration: {}
    With Traffic: {}

    """.format(
        start, start_address,
        end, end_address,
        dist_mi,
        duration_min,
        duration_traffic_min)

    print(output)


def query_trip_data(origin, dest):
    gmaps = _fetch_api_key()
    now = datetime.now()
    directions_result = gmaps.directions(origin,
                                         dest,
                                         mode="driving",
                                         departure_time=now)
    write_cache('{}_to_{}.txt'.format(origin, dest), directions_result)
    store_results(origin, dest, directions_result)
    return directions_result


def _fetch_api_key():
    print('Fetching api key...')

    save_obj(ApiAccessEvent())

    with open("maps.key", 'r') as f:
        return googlemaps.Client(f.readline())
