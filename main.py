from DurationQueries import query_trip_data

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


def run_single():
    if input('Use default origin/destination? Y/n\n') in set({'y', 'Y'}):
        query_trip_data(default_origin, default_dest)
    else:
        origin, dest = prompt_origin_dest()
        query_trip_data(origin, dest)


def run():
    start_options = """
    Select an option:
    1. Enter new query
    2. Run single query
    3. View data for query
    4. Run in background
    
    
    """

    start_operation = input(start_options)

    if start_operation == '1':
        prompt_origin_dest()
    elif start_operation == '2':
        run_single()
    elif start_operation == '3':
        prompt_data_to_view()
    else:
        print('Running queries in background...')


run()
