import sys

from DurationQueries import query_trip_data, fetch_api_key, fetch_client
from ImportQueries import store_csv_to_db
from MenuNavigation import *
from repository.DbOperations import fetch_duration_queries

regions_list = set({'sf', 'la', 'ny', 'dc', 'phx'})

default_origin = "333 twin dolphin drive"
default_dest = "555 california st"

other_origin = "Yamanakako Onsen Benifuji no Yu hot spring, 865-776 Yamanaka, Yamanakako, Minamitsuru District, Yamanashi 401-0501, Japan"
other_dest = "2-chōme-13-10 Asahi, Fujiyoshida, Yamanashi 403-0012, Japan"


def run_all_queries(client):
    queries = fetch_duration_queries()

    for duration_query in queries:
        query_trip_data(duration_query.name, duration_query.origin, duration_query.dest, client)


def run():
    is_done = False

    api_key = fetch_api_key()
    client = fetch_client(api_key)



    while not is_done:
        start_options = ['Run all queries',
                         'View data for query',
                         'View entries',
                         'Run in background',
                         'Import data from CSV']

        start_operation = prompt_menu(start_options, "Select an option:")

        if start_operation == 'Run all queries':
            run_all_queries(client)
        elif start_operation == 'Import data from CSV':
            store_csv_to_db()
        elif start_operation == 'Run in background':
            store_csv_to_db()
            sys.exit(1)

        else:
            print('Option not available (yet)')


run()
