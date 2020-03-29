from DurationQueries import query_trip_data

regions_list = set({'sf', 'la', 'ny', 'dc', 'phx'})


def build_query_map():
    query_map = {}

def enter_new_query():
    input_origin = input('Enter origin: ')
    input_dest = input('Enter destination: ')



def run():

    start_options = """
    1. Enter new query
    2. View data for query
    3. Run in background
    """



    start_operation = input('Enter new query (1) or continue with existing (2)?')

    if start_operation == '1':
        enter_new_query()

    data = query_trip_data(input_origin, input_dest)


origin = "333 twin dolphin drive"
dest = "555 california st"

other_origin = "Yamanakako Onsen Benifuji no Yu hot spring, 865-776 Yamanaka, Yamanakako, Minamitsuru District, Yamanashi 401-0501, Japan"
other_dest = "2-chōme-13-10 Asahi, Fujiyoshida, Yamanashi 403-0012, Japan"

run(other_origin, other_dest)
