import openai

openai.api_key = ""

MODEL = "gpt-3.5-turbo"
requests = [{"role": "system", "content": "You are a helpful assistant who provides answers within 50 words"}]

def get_response(request):
    global MODEL
    global requests
    requests.append({"role": "user", "content": request})
    chat = openai.ChatCompletion.create(
        model = MODEL,
        messages = requests
    )
    reply = chat.choices[0].message.content
    return reply

# chat = openai.ChatCompletion.create(
#   model="gpt-3.5-turbo",
#   messages=[
#         {"role": "system", "content": "You are a helpful assistant."},
#         {"role": "user", "content": "Who won the world series in 2020?"},
#         {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
#         {"role": "user", "content": "Where was it played?"}
#     ]
# )

# reply = chat.choices[0].message.content

# print(reply)
