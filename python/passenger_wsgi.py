import sys, os

from database_setup import Base, Criminal, Citation
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import cgi
from urlparse import urlparse
from flask import Flask
from flask import request, render_template, redirect, url_for
from telephony import *

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
    return render_template('index.html', criminals=criminals)

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

@application.route('/data/', methods=['GET', 'POST'])
def displayData():
    if request.method == 'GET':
        citations = session.query(Citation).all()
        return render_template('displaydata.html', citations=citations)

@application.route('/text/', methods=['POST'])
def send_sms():
    if request.method == 'POST':
        msg = request.form['message']
        client.messages.create(to="+17023284071", from_="+13342474764", body=msg)
        return redirect(url_for('index'))

@application.route('/twilio/', methods=['POST', 'GET'])
def receiveTwilio():
     if request.method == 'POST':
        msg = request.values.get('Body')
        from_number = request.values.get('From', None)

        if from_number in callers:
            message = callers[from_number] + ", thanks for being part of our experiment.  Your message was:" + msg
        else:
            message = "Something went wrong, your number is: " + str(from_number)

        resp = twilio.twiml.Response()
        resp.message(message)
        return str(resp)
