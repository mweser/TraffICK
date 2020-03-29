from repository.Database import *


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
