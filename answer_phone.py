from flask import Flask
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def answer_call():
    """Respond to incoming phone calls with a brief message."""
    # Start our TwiML response
    resp = VoiceResponse()

    # Read a message aloud to the caller
    audio = "Thank you for calling! Have a great day."
    resp.say(audio, voice='alice')
    resp.record()
    resp.hangup()

    return str(resp)

if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host = "127.0.0.1", port = "5000")
