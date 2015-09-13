__author__ = 'Sean'

import itertools
import csv
from sqlalchemy import Column, ForeignKey, Integer, String, UniqueConstraint, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Violation(Base):

    __tablename__ = 'violation'
    id = Column(Integer, primary_key=True)
    citation_number = Column(Integer, ForeignKey('citation.citation_number'), nullable=False)
    violation_number = Column(String(25))
    violation_description = Column(String(80))
    warrant_status = Column(String(15))
    warrant_number = Column(String(20))
    status = Column(String(50))
    status_date = Column(String(25))
    fine_amount = Column(String(15))
    court_cost = Column(String(15))

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

with open('violations.csv', 'r') as f:
    reader = csv.reader(f)
    columns = next(reader)

    while f:
        data = next(reader)
        v = Violation()
        v.id = data[0]
        v.citation_number =  data[1]
        v.violation_number = data[2]
        v.violation_description =  data[3]
        v.warrant_status =  data[4]
        v.warrant_number =  data[5]
        v.status =  data[6]
        v.status_date =  data[7]
        v.fine_amount =  data[8]
        v.court_cost =  data[9]
        session.add(v)
        session.commit()


