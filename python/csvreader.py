__author__ = 'Sean'

import itertools
import csv
from sqlalchemy import Column, ForeignKey, Integer, String, UniqueConstraint, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Citation(Base):

    __tablename__ = 'citation'
    id = Column(Integer, primary_key=True)
    citation_number = Column(Integer, unique=True)
    citation_date = Column(String(20))
    first_name = Column(String(20), nullable=False)
    last_name = Column(String(30), nullable=False)
    date_of_birth = Column(String(20))
    defendant_address = Column(String(90))
    defendant_city = Column(String(50))
    defendant_state = Column(String(2))
    drivers_license_number = Column(String(15))
    court_date = Column(String(20))
    court_location = Column(String(40))
    court_address = Column(String(90))

engine = create_engine('mysql://steveballmer:developers@crimelab.mocrime.thomasruble.com:3306/mocrime')
Base.metadata.create_all(engine)

DBSession = sessionmaker(bind=engine)
session = DBSession()

with open('citations.csv', 'r') as f:
    reader = csv.reader(f)
    columns = next(reader)
    while f:
        data = next(reader)
        cit = Citation()
        cit.id = data[0]
        cit.citation_number =  data[1]
        cit.citation_date =  data[2]
        cit.first_name =  data[3]
        cit.last_name =  data[4]
        cit.date_of_birth =  data[5]
        cit.defendant_address =  data[6]
        cit.defendant_city =  data[7]
        cit.defendant_state =  data[8]
        cit.drivers_license_number =  data[9]
        cit.court_date =  data[10]
        cit.court_location = data[11]
        cit.court_address =  data[12]
        session.add(cit)
        session.commit()


