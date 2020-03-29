import json
from datetime import datetime

import googlemaps


def _fetch_api_key():
    with open("maps.key", 'r') as f:
        return f.readline()


def write_results(filename, contents):
    with open(filename, 'w') as newfile:
        newfile.write(contents)


gmaps = googlemaps.Client(_fetch_api_key())

# Geocoding an address
geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions("69 clementina st, san francisco",
                                     "555 california st",
                                     mode="driving",
                                     departure_time=now)
# write_results("file_cache/syd_to_parramatta.txt", directions_result)

print(directions_result)
