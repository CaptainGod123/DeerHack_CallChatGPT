import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC32ddbde03b002e4253ea824e98261506'
auth_token = '3fe84d1da4b74e9e862beabf963ca1ba'
client = Client(account_sid, auth_token)

# from is twilio
# to is your number
call = client.calls.create(
                        url='http://demo.twilio.com/docs/voice.xml',
                        to='+14169867125',
                        from_='+16073501402'
                    )

print(call.sid)