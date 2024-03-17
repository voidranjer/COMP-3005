from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://postgres:myhotspot81@localhost:5432/assignment3')
Session = sessionmaker(bind=engine)

Base = declarative_base()