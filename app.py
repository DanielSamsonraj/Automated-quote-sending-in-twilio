from twilio.rest import Client
from bible_verses import get_message


account_sid = 'ACc828789a0014ae683094197c78eb1bff'
auth_token = 'bde52a496a3e9e1caf89d29401643a5e'
client = Client(account_sid, auth_token)


def send_msg():

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=get_message(),
        to='whatsapp:+918309282168'
    )

    print(message.sid)
