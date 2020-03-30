from DurationQueries import query_trip_data, fetch_api_key, fetch_client
from ImportQueries import store_csv_to_db
from MenuNavigation import *
from repository.DbOperations import fetch_duration_queries


def run_all_queries(client):
    queries = fetch_duration_queries()

    for duration_query in queries:
        query_trip_data(duration_query.name, duration_query.origin, duration_query.dest, client)
        if duration_query.bidirectional == '1':
            query_trip_data(duration_query.name + '_inv', duration_query.dest,
                            duration_query.origin, client)


def run():
    api_key = fetch_api_key()
    client = fetch_client(api_key)

    args = sys.argv
    if len(args) >= 2:
        if '-c' in args:
            print('Run cron')
            run_all_queries(client)
            return

    is_done = False

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
        elif start_operation == 'q':
            sys.exit(1)
        else:
            print('Option not available (yet)')

run()
