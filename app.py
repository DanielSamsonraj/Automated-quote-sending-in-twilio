from twilio.rest import Client
import requests
import random
from translate import Translator

account_sid = 'AC68981bf65fee38f68a59a56eac6b7486'
auth_token = '4b7cabfb977462f9211d8072c64030f2'
client = Client(account_sid, auth_token)

book_name = 'john '
chapter_no = '1'
verse_no = '1'

verse = requests.get('https://bible-api.com/' +
                     book_name + chapter_no + ':' + verse_no)

current_message = verse.json()['text']

translator = Translator(to_lang="Telugu")
translated_message = translator.translate(current_message)


def send_msg():
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=current_message + '\n' + translated_message,
        to='whatsapp:+918309282168'
    )

    print(message.sid)
