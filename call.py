import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC25bfc249b0eabe222892964cd4c3872d'
auth_token = '589de50df847fada596cb28c3fce526f'
client = Client(account_sid, auth_token)

call = client.calls.create(
                        url='http://demo.twilio.com/docs/voice.xml',
                        to='+14372160468',
                        from_='+16203878391'
                    )

print(call.sid)