import os
from datetime import datetime

from sqlalchemy import Column, Integer, String, Numeric, DateTime
from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_path = os.path.join(os.getenv("HOME"), ".sqlite/py_maps.db")

Base = declarative_base()


class ApiAccessEvent(Base):
    __tablename__ = 'api_access'
    query_time = Column(DateTime, primary_key=True, nullable=False, default=datetime.now())


class DurationQuery(Base):
    __tablename__ = 'duration_query'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(250), nullable=False)
    origin = Column(String(250), nullable=False)
    dest = Column(String(250), nullable=False)
    last_run = Column(DateTime, nullable=False, default=datetime.now())
    mode = Column(String(250), nullable=False, default='driving')
    region = Column(String(250), nullable=True)

class LocationCoordinates(Base):
    __tablename__ = 'location_coordinates'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(250), nullable=False)
    lat = Column(String(250), nullable=False)
    lon = Column(String(250), nullable=False)
    address = Column(String(250), nullable=False)


class DurationQueryResult(Base):
    __tablename__ = 'duration_query_result'
    id = Column(Integer, primary_key=True, autoincrement=True)
    query_time = Column(DateTime, nullable=False, default=datetime.now())
    origin_name = Column(String(250), nullable=False)
    dest_name = Column(String(250), nullable=False)
    duration_sec = Column(Integer, nullable=False)
    distance_m = Column(Integer, nullable=False)
    duration_traffic_sec = Column(Integer, nullable=False)
    distance_traffic_m = Column(Integer, nullable=False)
    mode = Column(String(250), nullable=False, default='driving')


tables_list = [LocationCoordinates, DurationQueryResult, DurationQuery, ApiAccessEvent]

engine = create_engine('sqlite:///{}'.format(db_path))
Base.metadata.create_all(engine)
Base.metadata.bind = engine


def save_obj(obj):
    try:
        session = sessionmaker(bind=engine)()
        session.add(obj)
        session.commit()
    except IntegrityError:
        print("Item already exists in data_repository: {}".format(str(obj)))


def remove_entries(table_type):
    session = sessionmaker(bind=engine)()
    session.query(table_type).delete()
    session.commit()
    print("Removed all entries from {}".format(table_type))
