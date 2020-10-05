import nltk
from nltk import word_tokenize

from urllib import request
from bs4 import BeautifulSoup

url = "https://www.myunidays.com"

# Ignore any issues with characters Python can't parse
htmlText = request.urlopen(url).read().decode('utf8', errors='ignore')


with open('document.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line)

# Removing HTML tags
content = BeautifulSoup(htmlText, 'html.parser').get_text()

print(content)