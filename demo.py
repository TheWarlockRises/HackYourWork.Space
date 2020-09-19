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


def work_timer(client, number, new_user, message):
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
    while time.time() - start < number:
        elapsed = time.time() - start
        if elapsed % 45 == 0:
            message = message + "You've accomplished a lot! It's time to get up and stretch, drink some water, and eat a " \
                                "snack!"
            try:
                snack_message = client.messages \
                    .create(
                    body=message,
                    from_='+13344908466',
                    to=new_user.phone
                )
            except TwilioRestException as e:
                print(e)
            print(snack_message.sid)
        elif elapsed % 30 == 0:
            message = message + " You're doing a great job! It's time to get up and stretch and drink some water!"
            try:
                drink_message = client.messages \
                    .create(
                    body=message,
                    from_='+13344908466',
                    to=new_user.phone
                )
            except TwilioRestException as e:
                print(e)
            print(drink_message.sid)
        elif elapsed % 18 == 0:
            message = message + " Hope you enjoyed the break! Let's keep your momentum going!"
            try:
                back_to_work_message = client.messages \
                    .create(
                        body=message,
                        from_='+13344908466',
                        to=new_user.phone
                    )
            except TwilioRestException as e:
                print(e)
            print(back_to_work_message.sid)
        elif elapsed % 15 == 0:
            message = message + " You're doing a great job! It's time to get up and stretch!"
            try:
                break_message = client.messages \
                    .create(
                    body=message,
                    from_='+13344908466',
                    to=new_user.phone
                )
            except TwilioRestException as e:
                print(e)
            print(break_message.sid)
    try:
        last_message = client.messages \
            .create(
            body="Congratulations, " + new_user.first + "! You've worked " + str(goal) + " " + units + "!",
            from_='+13344908466',
            to=new_user.phone
        )
    except TwilioRestException as e:
        print(e)

    print(last_message.sid)


f_name = 'Trey'
l_name = "D'Amico"
num = '+18302377042'
goal = 1
units = 'minute(s)'
secGoal = conversion(goal, units)
new_user = User(f_name, l_name, num, goal)
message_builder = "Hey there, " + new_user.first + "!"

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
