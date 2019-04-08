'''
POS-TAG using Scraping

#download

nltk.download('all')
'''
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from bs4 import BeautifulSoup
import requests
import re

def url_to_string(url):
    res = requests.get(url)
    html = res.text
    soup = BeautifulSoup(html, 'html5lib')
    for script in soup(["script", "style", 'aside']):
        script.extract()
    return " ".join(re.split(r'[\n\t]+', soup.get_text()))

ex_text = url_to_string('https://www.firstpost.com/business/a-year-after-pnb-fraud-lessons-learnt-from-nirav-modi-episode-but-some-questions-still-elude-answers-6085931.html')


def preprocess(sent):
    sent = nltk.word_tokenize(sent)
    sent = nltk.pos_tag(sent)
    return sent

sent = preprocess(ex_text)
sent

