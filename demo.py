from twilio.base.exceptions import TwilioRestException
from twilio.rest import Client
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from user import User
import time
import os
import datetime as date

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = os.environ['TWILIO_SID']
auth_token = os.environ['TWILIO_TOKEN']
client = Client(account_sid, auth_token)
finished = False

app = Flask(__name__)


@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    body = (request.values.get('Body', None)).lower()

    # Start our TwiML response
    resp = MessagingResponse()

    # Determine the right reply for this message
    if body == 'go':
        resp.message("Let's keep up the good work!")
        work_timer(client, secGoal, new_user, message_builder)
    elif body == 'stop':
        resp.message("The timer has stopped. Enjoy your break!")
    elif body == 'quit':
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
    except TwilioRestException as e:
        print(e)
    print(new_message.sid)


def work_timer(client, number, new_user, message):
    start = time.time()
    message_builder(" Time to get to work! You're going to accomplish great things!", new_user)
    while time.time() - start < number:
        elapsed = time.time() - start
        if elapsed % 45 == 0:
            message_builder(" You've accomplished a lot! It's time to get up and stretch, drink some water, and eat a " \
                                "snack!", new_user)
        elif elapsed % 30 == 0:
            message_builder(" You're doing a great job! It's time to get up and stretch and drink some water!", new_user)
        elif elapsed % 18 == 0:
            message_builder(" Hope you enjoyed the break! Let's keep your momentum going!", new_user)
        elif elapsed % 15 == 0:
            message_builder(" You're doing a great job! It's time to get up and stretch!", new_user)
    message_builder(" Congratulations, you've done a lot of wonderful things today! Can't wait to see what next time has in store!.", new_user)


f_name = 'Trey'
l_name = "D'Amico"
num = '+18302377042'
goal = 1
units = 'minute(s)'
secGoal = conversion(goal, units)
new_user = User(f_name, l_name, num, goal)

try:
    first_message = client.messages \
        .create(
            body=message_builder + "Ready to get started? Text GO when you're ready.",
            from_='+13344908466',
            to=new_user.phone
        )
except TwilioRestException as e:
    print(e)

print(first_message.sid)

app.run(host='0.0.0.0')
