import sqlite3
import random
from flask import Flask, jsonify, request
from twilio.twiml.voice_response import VoiceResponse, Gather
from ChatGPT import get_response
from flask_cors import CORS

from db_manipulation import add_user, add_message, check_and_setup_db, check_new_user

app = Flask(__name__)
cors = CORS(app)

@app.route("/", methods=['GET', 'POST'])
def answer_call():
    check_and_setup_db()


    phone_number = request.form.get('Caller')

    # provide a randome password if it is a new user
    rand = random.uniform(1, 9999)
    if check_new_user(phone_number) == 1:
        print ("the password id ")
        print (str(int(rand)))
        audio = "Welcome, "
        for i in range(1, len(str(phone_number))):
            audio = audio + str(phone_number)[i] + ' '
        audio = audio + ". This is CallGPT. Please memorize the following password to access your chat history. "
        for i in range(len(str(int(rand)))):
            audio = audio + str(int(rand))[i] + ' '
        audio = audio + ". How may I help you?"

        # add user to the db
        add_user(phone_number, int(rand))
    else:
        print(str(phone_number)[1:])
        audio = "Welcome back, "
        for i in range(1, len(str(phone_number))):
            audio = audio + str(phone_number)[i] + ' '
        audio = audio + ". This is CallGPT. How may I help you?"

    """Respond to incoming phone calls with a brief message."""
    # Start our TwiML response
    resp = VoiceResponse()

    # Read a message aloud to the caller
    gather = Gather(input='speech dtmf', action='/complete', speechModel="phone_call", speechTimeout = "1")


    gather.say(audio)
    resp.append(gather)

    add_message(phone_number, audio, True)
    return str(resp)


@app.route("/complete", methods=['POST'])
def get_msg():
    phone_number = request.form.get('Caller')

    print(f'SpeechResult:{request.form.get("SpeechResult")}, Confidence:{request.form.get("Confidence")}')

    response = VoiceResponse()
    user_request = parse_request()
    print(f"user: {user_request}")
    add_message(phone_number, user_request)

    # the result of ChatGPT
    if user_request is None:
        response.say("failed")
        return str(response)

    gpt_response = get_response(user_request)
    response.say(gpt_response)
    print(f"gpt: {gpt_response}")
    add_message(phone_number, gpt_response, True)

    response.pause(length = 1)
    audio = "Do you have any furthur questions? Hang up if you have no more questions."
    response.say(audio)
    add_message(phone_number, audio, True)

    gather = Gather(input='speech dtmf', action='/complete', speechModel="phone_call", speechTimeout = "1")
    response.append(gather)
    return str(response)


def parse_request():
    speech_result = request.form["SpeechResult"]
    confidence = request.form["Confidence"]
    print(confidence)
    return speech_result


@app.route('/users', methods=['GET'])
def get_users():
    check_and_setup_db()

    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()

    # Retrieve all rows from users table
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()

    # Convert rows to list of dictionaries
    users = []
    for row in rows:
        user = {'phone_number': row[0], 'password': row[1], 'conversation': row[2]}
        users.append(user)

    conn.close()

    return jsonify(users)

if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host = "127.0.0.1", port = "5000")
