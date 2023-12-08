import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = "AC3bddb2a31fe779a1f95f24a9b08c1cf7"
auth_token = "4664ad14f59c4e38cdd0bd9cfefd5612"
client = Client(account_sid, auth_token)

call = client.calls.create(
                        url='https://demo.twilio.com/welcome/voice/',
                        to='+261380611756',
                        from_='+15178169624'
                    )

print(call.sid)