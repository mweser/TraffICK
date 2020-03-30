import os


def read_cache(filename):
    with open(os.path.join('../file_cache/', filename), 'r') as f:
        return f.readline()


def write_cache(filename, contents):
    with open(os.path.join('../file_cache/', filename), 'w') as f:
        f.write(str(contents))
