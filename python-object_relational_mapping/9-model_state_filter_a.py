import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


engine = create_engine("mysql+mysqldb://{}:{}"
                       "@localhost/{}"
                       .format(sys.argv[1], sys.argv[2], sys.argv[3]))

Session = sessionmaker(bind=engine)
session = Session()
has_a = session.query(State).filter(State.name.like('%a%')).all()

for state in has_a:
    print("{}: {}".format(state.id, state.name))
