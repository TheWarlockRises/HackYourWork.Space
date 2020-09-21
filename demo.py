
from twilio.rest import Client
from flask import Flask, request, redirect
from flask_cors import CORS
from twilio.twiml.messaging_response import MessagingResponse
from user import User
import time
import os
import schedule
from pprint import pprint
import emoji

loopTime = 500 
goBreakSecs = 15
returnBreakSecs = 18
waterStretchSecs = 30
waterSnackSecs = 45

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
    user = User(json['fname'],json['lname'],json['num'],60 * (int(json['hours'])*60 + int(json['minutes'])))
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
        work_timer(users[inNumber])
    elif body == 'done':
        #will need to figure out how to stop the `scehdule` when this message comes in
        schedule.clear(tag=inNumber)
        resp.message("Sorry to see you go, but good job on what you've accomplished today!" + emoji.emojize(":grinning_face_with_big_eyes:"))

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


def work_timer(user):
    number = user.goal
    start = time.time()
    message_builder(" Time to get to work! You're going to accomplish great things! " + emoji.emojize(":hammer:") + "\nReply DONE to stop receiving reminders.", user)

    schedule.every(waterSnackSecs).seconds.do(message_builder, " You've accomplished a lot! " + emoji.emojize(":trophy:") + " It's time to get up and stretch " + emoji.emojize(":raising_hands:"), user).tag(user.phone)
    schedule.every(waterStretchSecs).seconds.do(message_builder, " You're doing a great job! " + emoji.emojize(":sports_medal:") + "It's time to drink some water!" + emoji.emojize(":droplet:"), user).tag(user.phone)
    schedule.every(returnBreakSecs).seconds.do(message_builder, " Hope you enjoyed the break! Let's keep your momentum going! " + emoji.emojize(":flexed_biceps:"), user).tag(user.phone)
    schedule.every(goBreakSecs).seconds.do(message_builder, " You're doing a great job! " + emoji.emojize(":clapping_hands:") + " It's time to get a snack! " + emoji.emojize(":pizza:"), user).tag(user.phone,'doOnce')

    while int(time.time() - start) < int(number):
        print(str(int(time.time() - start)) + "/" + str(int(number)))
        if((int(time.time() - start)) % (goBreakSecs + 2) != (int(time.time() - start)) % loopTime):
            schedule.clear(tag='doOnce')
        schedule.run_pending()
        time.sleep(1)

    message_builder(
        " Congratulations, you've done a lot of wonderful things today! Can't wait to see what next time has in store!. " + emoji.emojize(":partying_face:"),
        user)

app.run(host='0.0.0.0')
