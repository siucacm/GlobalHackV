__author__ = 'Sean'
import twilio.twiml
from twilio.rest import TwilioRestClient


account_sid = "AC7baad23321d71c42448deb02c3cb31ae"
auth_token = "4c35e0337dc3963f457d477c8a59996f"
client = TwilioRestClient(account_sid, auth_token)