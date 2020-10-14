import string
import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords

def removeStopwords(words):
    return [word for word in words if not word in string.punctuation]

stopwords = stopwords.words('english')

freqDist1 = FreqDist()
freqDist2 = FreqDist()

emma = nltk.corpus.gutenberg.raw('austen-emma.txt')
sense = nltk.corpus.gutenberg.raw('austen-sense.txt')

emma_tokens = removeStopwords(word_tokenize(emma))
sense_tokens = removeStopwords(word_tokenize(sense))

emma_vocab = nltk.Text(emma_tokens).vocab()
sense_vocab = nltk.Text(sense_tokens).vocab()

emma_bigrams = nltk.bigrams(emma_tokens)
sense_bigrams = nltk.bigrams(sense_tokens)

for token in emma_bigrams:
    freqDist1[token] += 1

for token in sense_bigrams:
    freqDist2[token] += 1

print("Bigrams")
print(freqDist1.most_common(10), end="...")
print()
print(freqDist2.most_common(10), end="...")

print("\nSingle tokens\n")

print(emma_vocab.most_common(10), end="...")
print()
print(sense_vocab.most_common(10), end="...")

# There are far more single tokens that repeat than bigrams that repeat - but that makes sense