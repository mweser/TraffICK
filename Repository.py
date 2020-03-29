# import os
# from datetime import datetime
#
# from sqlalchemy import Column, Integer, String, Numeric, Date, DateTime
# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
#
# db_path = os.path.join(os.getenv("HOME"), ".sqlite/py_maps.db")
#
#
# Base = declarative_base()
#
#
# class Results(Base):
#     __tablename__ = 'credit_payment_event'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     results_blob = Column(String(250), nullable=False)
#     payment_date = Column(Date, nullable=False, default=datetime.now())
#
#
# tables_list = []
#
# engine = create_engine('sqlite:///{}'.format(db_path))
# Base.metadata.create_all(engine)
# Base.metadata.bind = engine
