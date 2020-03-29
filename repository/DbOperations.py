from repository.Database import *


def address_exists(address):
    session = sessionmaker(bind=engine)()
    query = session \
        .query(LocationCoordinates) \
        .filter_by(address=address) \
        .all()

    result = len(query) == 1

    if result:
        print('LocationCoordinates \'{}\' exists'.format(address))
    return result


def duration_query_exists(name):
    session = sessionmaker(bind=engine)()
    query = session \
        .query(DurationQuery) \
        .filter_by(name=name) \
        .all()

    result = len(query) == 1

    if result:
        print('DurationQuery \'{}\' exists'.format(name))
    return result


def fetch_duration_queries():
    session = sessionmaker(bind=engine)()
    query = session \
        .query(DurationQuery) \
        .all()
    return query
