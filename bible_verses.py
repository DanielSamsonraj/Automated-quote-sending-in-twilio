import requests
import random
from translate import Translator
from bs4 import BeautifulSoup


def TodaysVerse():
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
    return verse_number + verse


def get_message():
    current_message = TodaysVerse()
    return current_message
