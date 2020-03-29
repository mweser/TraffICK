import os
from datetime import datetime

from sqlalchemy import Column, Integer, String, Numeric, DateTime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

db_path = os.path.join(os.getenv("HOME"), ".sqlite/py_maps.db")

Base = declarative_base()


class DurationQuery(Base):
    __tablename__ = 'duration_query_result'
    id = Column(Integer, primary_key=True, autoincrement=True)
    origin = Column(String(250), nullable=False)
    dest = Column(String(250), nullable=False)
    last_run = Column(DateTime, nullable=False, default=datetime.now())
    mode = Column(String(250), nullable=False, default='driving')


class LocationCoordinates(Base):
    __tablename__ = 'location_coordinates'
    name = Column(String(250), nullable=False)
    lat = Column(String(250), nullable=False)
    lon = Column(String(250), nullable=False)


class DurationQueryResult(Base):
    __tablename__ = 'duration_query_result'
    id = Column(Integer, primary_key=True, autoincrement=True)
    query_time = Column(DateTime, nullable=False, default=datetime.now())
    origin_name = Column(String(250), nullable=False)
    dest_name = Column(String(250), nullable=False)
    duration_min = Column(Integer, nullable=False)
    duration_sec = Column(Integer, nullable=False)
    distance_mi = Column(Numeric, nullable=False)
    distance_m = Column(Integer, nullable=False)
    mode = Column(String(250), nullable=False, default='driving')


tables_list = [LocationCoordinates, DurationQueryResult, DurationQuery]

engine = create_engine('sqlite:///{}'.format(db_path))
Base.metadata.create_all(engine)
Base.metadata.bind = engine
