from django.shortcuts import render
from django.http import HttpResponse
from twilio.rest import Client
from django.conf import settings
# Create your views here.  

to = '+917470400587'
client = Client(settings.TWILIO_ACCOUNT_SID,settings.TWILIO_AUTH_TOKEN)
response = client.messages.create(body='Hello testing twilio',to=to,from_=settings.TWILIO_PHONE_NUMBER)
