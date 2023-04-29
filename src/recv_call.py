from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse, Gather, Say
from chatgpt import get_response

app = Flask(__name__)

def welcome():
    response = VoiceResponse()

INITIAL_CONVERSATION = True

@app.route("/answer", methods=['GET', 'POST'])
def answer_call():
    """Respond to incoming phone calls with a brief message."""
    global INITIAL_CONVERSATION
    response = VoiceResponse()
    if not INITIAL_CONVERSATION:
        user_request = parse_request()
        print(f"user: {user_request}")
        if user_request is None:
            response.say("failed")
            return str(response)
        else:
            gpt_response = get_response(user_request)
            print(f"gpt: {gpt_response}")
            response.say(gpt_response)
            response.pause(length=1)

    gather = Gather(input='speech dtmf', action='/answer', speechModel="phone_call")
    gather.say('How can I help you?' if INITIAL_CONVERSATION else 'Do you have any furthur questions?')
    response.append(gather)

    # response.say("Received")

    INITIAL_CONVERSATION = False

    return str(response)

def parse_request():
    speech_result = request.form["SpeechResult"]
    confidence = request.form["Confidence"]
    print(confidence)
    return speech_result


@app.route("/complete", methods=['POST'])
def get_msg():
    print(f'SpeechResult:{request.form.get("SpeechResult")}, Confidence:{request.form.get("Confidence")}')
    response = VoiceResponse()
    response.say("complete")
    return str(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
