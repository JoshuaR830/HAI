import nltk
from nltk import word_tokenize
from nltk import pos_tag

emma = nltk.corpus.gutenberg.raw('austen-emma.txt')

tokens = word_tokenize(emma)

text = nltk.Text(tokens)

vocabulary = text.vocab()

def printWord(word):
    if(word.lower().startswith('wh')):
        return True
    return False

whWords = list(filter(printWord, tokens))

whVocab = nltk.Text(whWords).vocab()
print(whVocab.most_common())
print("\n\n")

# To clean up some words use Part of Speech tagging

def removeNounsAndAdjectives(words_list):
    pos_tagged_wh_words = pos_tag(words_list, tagset="universal")
    # print(pos_tagged_wh_words)

    cleaned_list = [item[0] for item in pos_tagged_wh_words if(item[1] != "NOUN" and item[1] != "ADJ")]
    
    return cleaned_list

cleanedList = removeNounsAndAdjectives(whWords)
cleanText = nltk.Text(cleanedList)
cleanVocab = cleanText.vocab()
print(cleanVocab.most_common())

# Repetition: What what wholoesome. whoelesome...