from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse, Gather

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def answer_call():
    """Respond to incoming phone calls with a brief message."""
    # Start our TwiML response
    resp = VoiceResponse()

    # Read a message aloud to the caller
    gather = Gather(input='speech dtmf', action='/complete', speechModel="phone_call")
    audio = "This is ChatGPT. How may I help you?"
    gather.say(audio, voice='alice')
    resp.append(gather)

    return str(resp)

@app.route("/complete", methods=['POST'])
def get_msg():
    print(f'SpeechResult:{request.form.get("SpeechResult")}, Confidence:{request.form.get("Confidence")}')
    response = VoiceResponse()
    # the result from ChatGPT shold be placed here
    audio = "You just said: " + request.form.get("SpeechResult")
    response.say(audio) 
    return str(response)

# @app.route("/ask", methods=['GET', 'POST'])
# def answer_call():
#     """Respond to incoming phone calls with a brief message."""
#     # Start our TwiML response
#     resp = VoiceResponse()

#     # Read a message aloud to the caller
#     gather = Gather(input='speech dtmf', action='/complete', speechModel="phone_call")
#     audio = "This is ChatGPT. How may I help you?"
#     gather.say(audio, voice='alice')
#     resp.append(gather)

#     return str(resp)

if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host = "127.0.0.1", port = "5000")
