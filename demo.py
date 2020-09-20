from twilio.base.exceptions import TwilioRestException
from twilio.rest import Client
from flask import Flask, request, redirect
from flask_cors import CORS
from twilio.twiml.messaging_response import MessagingResponse
from user import User
import time
import os
import datetime as date
import schedule
from pprint import pprint

account_sid = os.environ['TWILIO_SID']
auth_token = os.environ['TWILIO_TOKEN']
client = Client(account_sid, auth_token)
finished = False
users = {}
app = Flask(__name__)
CORS(app)

@app.route("/userupdate",methods=['POST'])
def update_user():
    json = request.json
    pprint(json)
    user = User(json['fname'],json['lname'],json['num'],60 * (json['hours']*60 + json['minutes']))
    message_builder("Ready to get started? Text GO to start",user)
    users[user.phone] = user
    return ("OK")

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    pprint(request.values)
    body = (request.values.get('Body', None)).lower()
    inNumber = request.values.get('From', None)
    # Start our TwiML response
    resp = MessagingResponse()

    if inNumber not in users:
        resp.message("Sorry, you're not registered to use this service")
        return str(resp)

    # Determine the right reply for this message
    if body == 'go':

        #this resp is sent late because work_timer blocks the return statement
        #resp.message("Let's keep up the good work!")
        work_timer(client, users[inNumber])
    elif body == 'done':
        #will need to figure out how to stop the `scehdule` when this message comes in
        schedule.clear(tag=inNumber)
        resp.message("Sorry to see you go, but good job on what you've accomplished today")

    return str(resp)


def conversion(number, state):
    if state == "minute(s)":
        return number * 60
    if state == "hour(s)":
        return number * 3600

def message_builder(message, user):
    message_base = "Hey there, " + user.first + "! "
    try:
        new_message = client.messages \
            .create(
            body=message_base + message,
            from_='+13344908466',
            to=user.phone
        )
        print(new_message.sid)
    except TwilioRestException as e:
        print(e)


def work_timer(client, user):
    number = user.goal
    start = time.time()
    message_builder(" Time to get to work! You're going to accomplish great things! \n Reply DONE to stop receiving reminders.", user)

    schedule.every(45).seconds.do(message_builder, " You've accomplished a lot! It's time to get up and stretch, drink some water, and eat a snack!", user).tag(user.phone)
    schedule.every(30).seconds.do(message_builder, " You're doing a great job! It's time to get up and stretch and drink some water!", user).tag(user.phone)
    schedule.every(18).seconds.do(message_builder, " Hope you enjoyed the break! Let's keep your momentum going!", user).tag(user.phone)
    schedule.every().minutes.at(":15").do(message_builder, " You're doing a great job! It's time to get up and stretch!", user).tag(user.phone)

    while int(time.time() - start) < int(number):
        schedule.run_pending()
        time.sleep(1)

    message_builder(
        " Congratulations, you've done a lot of wonderful things today! Can't wait to see what next time has in store!.",
        user)

app.run(host='0.0.0.0')
