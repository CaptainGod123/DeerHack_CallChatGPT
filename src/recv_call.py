from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse, Gather, Say

app = Flask(__name__)


@app.route("/answer", methods=['GET', 'POST'])
def answer_call():
    # """Respond to incoming phone calls with a brief message."""
    # # Start our TwiML response
    # resp = VoiceResponse()

    # # Read a message aloud to the caller
    # resp.say("Thank you for calling! Have a great day.", voice='alice')

    # return str(resp)

    response = VoiceResponse()
    gather = Gather(input='speech dtmf', action='/complete', speechModel="phone_call")
    gather.say('Welcome to Twilio')
    response.append(gather)

    return str(response)


@app.route("/complete", methods=['POST'])
def get_msg():
    print(f'SpeechResult:{request.form.get("SpeechResult")}, Confidence:{request.form.get("Confidence")}')
    response = VoiceResponse()
    response.say("complete")
    return str(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0")