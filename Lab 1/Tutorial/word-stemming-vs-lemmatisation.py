import nltk
from nltk.tokenize import word_tokenize

# sentence = "One cat jumps, two cats jump"
sentence = "This is a test sentence, and I am hoping it doesn't get chopped up too much."
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
# Dictionary based
# Uncover the morphological root of a word
# Slower - more meaningful results
from nltk.stem.wordnet import WordNetLemmatizer
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('universal_tagset')

lemmatiser = WordNetLemmatizer()

# Lemmatiser is set to assume everyhting is a noun by default

for token in word_tokenize(sentence):
    print(lemmatiser.lemmatize(token))
    print('---')

tagged_words = nltk.pos_tag(word_tokenize(sentence))
print(tagged_words)

postmap = {
    'ADJ': 'j',
    'NOUN': 'n',
    'VERB': 'v',
    'ADV': 'r'
}

better_tagged_words = nltk.pos_tag(word_tokenize(sentence), tagset='universal')
print(better_tagged_words)

for token in better_tagged_words:
    word = token[0]
    tag = token[1]
    if tag in postmap.keys():
        print(lemmatiser.lemmatize(word, postmap[tag]))
    else:
        print(lemmatiser.lemmatize(word))
    print('---')


