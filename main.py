from datetime import datetime

import googlemaps


def _fetch_api_key():
    with open("maps.key", 'r') as f:
        return googlemaps.Client(f.readline())


def write_results(filename, contents):
    with open(filename, 'w') as newfile:
        newfile.write(contents)


def query_trip_data(origin, dest):
    gmaps = _fetch_api_key()
    now = datetime.now()
    directions_result = gmaps.directions(origin,
                                         dest,
                                         mode="driving",
                                         departure_time=now)
    print(directions_result)


origin = "333 twin dolphin drive"
dest = "555 california st"

query_trip_data(origin, dest)
