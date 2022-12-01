from datetime import date as dt
import os
from twilio.rest import Client
import json
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from operator import le

today_date = dt.today()
# Textual month, day and year
d2 = today_date.strftime("%m-%d-%Y")
# end of current date variable




class Accountability:
    def Date_Notifcation(self):
        # Find your Account SID and Auth Token at twilio.com/console
        # and set the environment variables. See http://twil.io/secure
        account_sid = os.environ['AC6ceaadc0e4eaba860afa41bf69b96bd8']
        print(type(account_sid))
        print(account_sid)

        auth_token = os.environ['TWILIO_AUTH_TOKEN']
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body='Hi there',
            from_='+15017122661',
            to='+15558675310'
        )

        print(message.sid)


