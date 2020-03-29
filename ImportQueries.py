import csv

from repository.Database import *
from repository.DbOperations import duration_query_exists

valid_true = set({'yes', 'y', 't', 'true'})
valid_false = set({'no', 'n', 'f', 'false'})


def parse_mode(data):
    if data == '':
        return 'driving'
    return data


def parse_bidirectional(data):
    return str(data.lower() in valid_false)


def store_csv_to_db(filename='query_list/queries.csv'):
    entries = _import_csv_to_dict(filename)

    for entry in entries:
        if not duration_query_exists(entry['name']):
            new_query = DurationQuery(
                name=entry['name'],
                origin=entry['origin'],
                dest=entry['destination'],
                mode=parse_mode(entry['mode']),
                region=entry['region_code'],
                bidirectional=parse_bidirectional(entry['bidirectional']))
            print('Saving new query:'
                  'name: {}'
                  'origin: {}'
                  'dest: {}'
                  'mode: {}'
                  'region: {}'
                  'bidirectional: {}'.format(
                entry['name'],
                entry['origin'],
                entry['destination'],
                entry['mode'],
                entry['region_code'],
                entry['bidirectional']))

            save_obj(new_query)


def _import_csv_to_dict(filename='query_list/queries.csv'):
    print("Importing data from {}".format(filename))

    data = []
    with open(filename, "r") as newfile:
        csv_reader = csv.DictReader(newfile)
        for line in csv_reader:
            data.append(line)
    return data
