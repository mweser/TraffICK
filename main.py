import os
from datetime import datetime

import googlemaps


def _fetch_api_key():
    with open("maps.key", 'r') as f:
        return googlemaps.Client(f.readline())


def write_results(filename, contents):
    with open(os.path.join('file_cache/', filename), 'w') as newfile:
        newfile.write(str(contents))


def query_trip_data(origin, dest):
    gmaps = _fetch_api_key()
    now = datetime.now()
    directions_result = gmaps.directions(origin,
                                         dest,
                                         mode="driving",
                                         departure_time=now)
    write_results('rws_to_555.txt', directions_result)
    print(directions_result)


origin = "333 twin dolphin drive"
dest = "555 california st"

query_trip_data(origin, dest)
