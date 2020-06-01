from twilio.rest import Client
from bible_verses import get_message


account_sid = 'XXXXXXXXXXXXXXXXXXXXX'
auth_token = 'XXXXXXXXXXXXXXXXXXXXXXX'
client = Client(account_sid, auth_token)


def send_msg():

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=get_message(),
        to='whatsapp:+918309282168'
    )

    print(message.sid)
