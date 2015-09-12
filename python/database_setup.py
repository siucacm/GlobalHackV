__author__ = 'Sean'
import os, sys
INTERP = os.path.expanduser("/home/thorub2/MOcrime.thomasruble.com/env/bin/python")
if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)

from sqlalchemy import Column, ForeignKey, Integer, String, UniqueConstraint, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Ticket(Base):

    __tablename__ = 'ticket'
    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)

class Criminal(Base):

    __tablename__ = 'criminal'
    name = Column(String(90), nullable=False)
    id = Column(Integer, primary_key=True)
    infraction = Column(String(90))


class Citation(Base):

    __tablename__ = 'citation'
    id = Column(Integer, primary_key=True)
    citation_number = Column(Integer, unique=True)
    citation_date = Column(DateTime, timezone=False)
    first_name = Column(String(20), nullable=False)
    last_name = Column(String(30), nullable=False)
    date_of_birth = Column(DateTime)
    defendant_address = Column(String(90))
    defendant_city = Column(String(50))
    defendant_state = Column(String(2))
    drivers_license_number = Column(String(15))
    court_date = Column(DateTime)






##end
engine = create_engine('mysql://steveballmer:developers@crimelab.mocrime.thomasruble.com:3306/mocrime')
Base.metadata.create_all(engine)
