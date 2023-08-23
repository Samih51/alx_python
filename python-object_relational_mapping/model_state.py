import sys

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

path = "mysql+mysqldb://{}:{}@localhost/{}".format(sys.argv[1], sys.argv[2], sys.argv[3])

database = create_engine(path, echo=True)
connection = database.connect()


Base = declarative_base()

"""the state class"""
class State(Base):
    """this is a class about state"""

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name =  Column(String(128))

    def __init__(self,name):
        self.name = name

Base.metadata.create_all(bind=database)