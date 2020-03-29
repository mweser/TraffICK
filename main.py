def _fetch_api_key():
    with open("api.key", 'r') as f:
        return f.readline()


print("Hello there! Key: {}".format(_fetch_api_key()))
