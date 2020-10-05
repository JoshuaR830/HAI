import nltk
from urllib import request


# This uses a specific corpus
nltk.download('gutenberg')

print(nltk.corpus.gutenberg.fileids())


# Download new documents like This
url = "http://example.org"
raw = request.urlopen(url).read().decode('utf8')
print(raw)
