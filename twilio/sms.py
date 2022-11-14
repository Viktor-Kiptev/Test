from twilio.rest import Client
import twilio_config
number_to =

account_sid = twilio_config.acc_sid
auth_token = twilio_config.auth_token
client = Client(account_sid, auth_token)

message = client.messages.create(
    messaging_service_sid='MG325dee379a39e6c3d2b76c4d3fc3cff6',
    body='Test #2',
    to='some_number'
)

print(message.sid)
