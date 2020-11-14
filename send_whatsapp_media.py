# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
from decouple import config


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure

account_sid = config('TWILIO_ACCOUNT_SID') 
auth_token =  config('AUTH_TOKEN') 
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         media_url=['https://images.unsplash.com/photo-1545093149-618ce3bcf49d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=668&q=80'],
         from_='whatsapp:+14155238886',
         body="It's Manus time!",
         to='whatsapp:+4915738378218'
     )

print(message.sid)

