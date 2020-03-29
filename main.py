from DurationQueries import query_trip_data
from ImportQueries import store_csv_to_db
from MenuNavigation import *

regions_list = set({'sf', 'la', 'ny', 'dc', 'phx'})

default_origin = "333 twin dolphin drive"
default_dest = "555 california st"

other_origin = "Yamanakako Onsen Benifuji no Yu hot spring, 865-776 Yamanaka, Yamanakako, Minamitsuru District, Yamanashi 401-0501, Japan"
other_dest = "2-chōme-13-10 Asahi, Fujiyoshida, Yamanashi 403-0012, Japan"


def build_query_map():
    query_map = {}


def prompt_origin_dest():
    input_origin = input('Enter origin: ')
    input_dest = input('Enter destination: ')

    return input_origin, input_dest


def prompt_data_to_view():
    pass


def run_single(use_default=False):
    if use_default:
        query_trip_data(default_origin, default_dest)
    else:
        origin, dest = prompt_origin_dest()
        query_trip_data(origin, dest)


def run():
    start_options = ['Run default configuration',
                     'Run single query',
                     'View data for query',
                     'View entries',
                     'Run in background',
                     'Import data from CSV']

    start_operation = prompt_menu(start_options, "Select an option:")

    if start_operation == 'Run default configuration':
        run_single(use_default=True)
    elif start_operation == 'Run single query':
        run_single(use_default=False)
    elif start_operation == 'Import data from CSV':
        store_csv_to_db()
    else:
        print('Running queries in background...')


run()
