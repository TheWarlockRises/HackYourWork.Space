from twilio.base.exceptions import TwilioRestException
from twilio.rest import Client
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from user import User
import time
import os

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = os.environ['TWILIO_SID']
auth_token = os.environ['TWILIO_TOKEN']
client = Client(account_sid, auth_token)

app = Flask(__name__)


@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Start our TwiML response
    resp = MessagingResponse()

    # Add a message
    resp.message("The Robots are coming! Head for the hills!")

    return str(resp)


def conversion(number, state):
    if state == "minute(s)":
        return number * 60
    if state == "hour(s)":
        return number * 3600


def work_timer(client, number, new_user):
    start = time.time()
    try:
        first_message = client.messages \
            .create(
            body="Time to get to work.",
            from_='+13344908466',
            to=new_user.phone
        )
    except TwilioRestException as e:
        print(e)
    print(first_message.sid)
    time.sleep(number)
    end = time.time()
    return end - start


f_name = 'Trey'
l_name = "D'Amico"
num = '+18302377042'
goal = 1
units = 'minute(s)'
secGoal = conversion(goal, units)
new_user = User(f_name, l_name, num, goal)

"""elapsed_time = work_timer(client, secGoal, new_user)"""

try:
    last_message = client.messages \
        .create(
            body="Congratulations! You've worked " + str(goal) + " " + units + "!",
            from_='+13344908466',
            to=new_user.phone
        )
except TwilioRestException as e:
    print(e)

print(last_message.sid)

app.run(debug=True)
