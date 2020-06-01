from twilio.rest import Client
from bible_verses import get_message


account_sid = 'ACc828789a0014ae683094197c78eb1bff'
auth_token = '9b87279682528ae846648ea4fb34e5b4'
client = Client(account_sid, auth_token)


def send_msg():

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=get_message(),
        to='whatsapp:+918309282168'
    )

    print(message.sid)
