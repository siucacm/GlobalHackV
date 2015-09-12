__author__ = 'Sean'
import os, sys
INTERP = os.path.expanduser("/home/thorub2/MOcrime.thomasruble.com/env/bin/python")
if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)

from sqlalchemy import Column, ForeignKey, Integer, String
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


class Citation(Base)

	__table

##end
engine = create_engine('mysql://steveballmer:developers@crimelab.mocrime.thomasruble.com:3306/mocrime')
Base.metadata.create_all(engine)
