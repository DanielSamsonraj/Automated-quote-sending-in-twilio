import requests
import random
from translate import Translator
from bs4 import BeautifulSoup

page = requests.get('https://www.christianity.com/bible/dbv.php')
soup = BeautifulSoup(page.content, "html.parser")
data = soup.findAll("div", {"class": "row margin-top-20"})
data1 = data[0].findAll("div", {"class": "col-md-12"})
message = data1[0].find("blockquote").get_text()
message = message.split(" ")
verse = ""
for msg in message:
    if msg != '':
        verse += msg + " "
verseNO = data1[0].find("a").get_text()
verseNO = verseNO.split(" ")

verse_number = ""
for msg in verseNO:
    if msg != '':
        verse_number += msg + " "
print(verse_number, verse)


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
