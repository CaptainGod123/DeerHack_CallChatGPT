from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse, Gather
from ChatGPT import get_response

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def answer_call():
    """Respond to incoming phone calls with a brief message."""
    # Start our TwiML response
    resp = VoiceResponse()

    # Read a message aloud to the caller
    gather = Gather(input='speech dtmf', action='/complete', speechModel="phone_call", speechTimeout = "1")
    audio = "This is ChatGPT. How may I help you?"
    gather.say(audio)
    resp.append(gather)

    return str(resp)

@app.route("/complete", methods=['POST'])
def get_msg():
    print(f'SpeechResult:{request.form.get("SpeechResult")}, Confidence:{request.form.get("Confidence")}')
    
    response = VoiceResponse()
    # the result of ChatGPT 
    user_request = parse_request()
    print(f"user: {user_request}")
    if user_request is None:
        response.say("failed")
        return str(response)
    else:
        gpt_response = get_response(user_request)
        print(f"gpt: {gpt_response}")
        response.say(gpt_response)
        response.pause(length = 1)
    
    
    audio = "Do you have any furthur questions?"
    response.say(audio) 
    
    
    gather = Gather(input='speech dtmf', action='/complete', speechModel="phone_call", speechTimeout = "1")
    response.append(gather)
        
        
        
    return str(response)


def parse_request():
    speech_result = request.form["SpeechResult"]
    confidence = request.form["Confidence"]
    print(confidence)
    return speech_result

if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host = "127.0.0.1", port = "5000")
