from twilio.rest import Client
from bible_verses import get_message


account_sid = 'AC68981bf65fee38f68a59a56eac6b7486'
auth_token = '81da9f6e09ba7f428936a1480b4f5279'
client = Client(account_sid, auth_token)


def send_msg():

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=get_message(),
        to='whatsapp:+918309282168'
    )

    print(message.sid)
