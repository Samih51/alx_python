"""this imports sys"""
import sys

"""This script demonstrates the use of SQLAlchemy to connect to a MySQL database."""
from sqlalchemy import create_engine
"""This script demonstrates the use of SQLAlchemy to connect to a MySQL database."""
from sqlalchemy.ext.declarative import declarative_base
"""This script demonstrates the use of SQLAlchemy to connect to a MySQL database."""
from sqlalchemy import Column, Integer, String

path = "mysql+mysqldb://{}:{}@localhost/{}".format(sys.argv[1], sys.argv[2], sys.argv[3])

database = create_engine(path, echo=True)
connection = database.connect()


Base = declarative_base()

"""the state class"""
class State(Base):
    """Represents a state entity in the database."""

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name =  Column(String(128))

    def __init__(self,name):
        """Initialize a State object with a name."""
        self.name = name

Base.metadata.create_all(bind=database)