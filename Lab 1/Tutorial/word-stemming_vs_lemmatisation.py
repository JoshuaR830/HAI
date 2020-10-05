import nltk
from nltk.tokenize import word_tokenize

sentence = "One cat jumps, two cats jump"
print(sentence)

# Stemming
# Faster than lammatisation - common part of inflection of word
# Need different stemmers for different languages
# Heuristics used to find most likely stem of the word

from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.lancaster import LancasterStemmer

p_stemmer = PorterStemmer()
s_stemmer = SnowballStemmer('english')
l_stemmer = LancasterStemmer()


for token in word_tokenize(sentence):
    print(p_stemmer.stem(token))
    print(s_stemmer.stem(token))
    print(l_stemmer.stem(token))
    print('---')

print("vs")

# Lemmatisation
from nltk.stem.wordnet import wordNetLemmatizer
nltk.download('wordnet')

lemmatiser = wordNetLemmatizer()

for token in word_tokenize(sentence):
    print(lemmatiser.lemmatize(token))
    print('---')