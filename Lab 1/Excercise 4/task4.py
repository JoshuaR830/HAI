# Given string s
# Given a number n
# Return the top n tokens (words) by decreasing frequency

# Should use the vocab() method of a text object
# Gives text in form of a dictionary
# Key is the token
# Value is number of occurrences

from nltk.text import Text
import nltk.corpus

def calculateFrequency(text, n):
    vocabulary = text.vocab()

    for x in range(n):
        word = vocabulary.most_common()[x][0]
        numOccur = vocabulary.most_common()[x][1]
        print(f"{x+1}. {word} x{numOccur}")

def characterTopN(s, n):
    calculateFrequency(Text(s), n)

def wordTopN(s, n):
    calculateFrequency(Text(s.split()), n)

sentence = "If Peter Piper picked a peck of pickled peppers, how many pickled peppers did Peter Piper pick"

# characterTopN(sentence, 3)
wordTopN(sentence, 8)