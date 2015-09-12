import sys, os

from database_setup import Base, Ticket, Criminal
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import cgi
from urlparse import urlparse
from flask import Flask
from flask import request, render_template, redirect, url_for

INTERP = os.path.expanduser("/home/thorub2/MOcrime.thomasruble.com/env/bin/python")
if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)
sys.path.append(os.getcwd())

application = Flask(__name__)

engine = create_engine('mysql://steveballmer:developers@crimelab.mocrime.thomasruble.com:3306/mocrime')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


@application.context_processor
def utility_processor():
    return dict(str=str)

@application.route('/')
@application.route('/index/')
def index():
    criminals = session.query(Criminal).all()
    output = "<h3>The Hype Train is full steam ahead</h3><br>"
    for c in criminals:
      output += str(c.id) + " " + c.name + "<br>"
      output += "<b>CRIME:</b><em> " + c.infraction + "</em>"
      output += "<br><br>"
    output += "<a href=/newcriminal/>New criminal</a>"
    return output

@application.route('/newcriminal/', methods=['GET', 'POST'])
def newCriminal():
    if request.method == 'POST':
        name = request.form['name']
	infraction = request.form['infraction']
        if name:
            newCriminal = Criminal(name=name, infraction=infraction)
            session.add(newCriminal)
            session.commit()
        return redirect(url_for('index'))
    else:
        return render_template('newCriminal.html')


