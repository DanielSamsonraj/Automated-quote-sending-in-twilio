import requests
import random
from translate import Translator
references = [
    {
        'book_name': 'romans ',
        'chapter_no': '8:',
        'verse_no': '38',
    },
    {
        'book_name': 'lamentations ',
        'chapter_no': '3:',
        'verse_no': '22',
    },
    {
        'book_name': 'john ',
        'chapter_no': '15:',
        'verse_no': '13',
    },
    {
        'book_name': 'ephesians ',
        'chapter_no': '3:',
        'verse_no': '20',
    },
    {
        'book_name': 'deuternomy ',
        'chapter_no': '31:',
        'verse_no': '6',
    },
    {
        'book_name': 'Psalm ',
        'chapter_no': '27:',
        'verse_no': '12',
    }
]


def get_message():

    random_no = random.randrange(0, len(references))

    query = references[random_no]['book_name'] + \
        references[random_no]['chapter_no'] + references[random_no]['verse_no']

    verse = requests.get('https://bible-api.com/' + query)

    current_message = verse.json()['text']

    translator = Translator(to_lang="Telugu")
    translated_message = translator.translate(current_message)

    translated_query = translator.translate(query)

    translated_message += '\n' + translated_query

    current_message = verse.json()['text'] + query + '\n'

    return current_message + translated_message
