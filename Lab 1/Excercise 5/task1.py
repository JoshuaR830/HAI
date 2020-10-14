import nltk
import math
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

from nltk.stem.porter import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer

from enum import Enum

emma = nltk.corpus.gutenberg.raw('austen-emma.txt')
sense = nltk.corpus.gutenberg.raw('austen-sense.txt')

stopwords = set(stopwords.words('english'))

class SimilarityType(Enum):
    JACCARD = 1
    EUCLIDEAN = 2
    MANHATTAN = 3


def similarity(s1, s2, similarityType = SimilarityType.EUCLIDEAN):
    s1_tokens = word_tokenize(s1)
    s2_tokens = word_tokenize(s2)

    toStem = False
    toLemmatize = False

    s1_no_stopwords = []
    s2_no_stopwords = []

    if toStem:
        stemmer = PorterStemmer()
        s1_no_stopwords = [stemmer.stem(token.lower()) for token in s1_tokens if not token.lower() in stopwords]
        s2_no_stopwords = [stemmer.stem(token.lower()) for token in s2_tokens if not token.lower() in stopwords]
    elif toLemmatize:
        lemmatizer = WordNetLemmatizer()
        s1_no_stopwords = [lemmatizer.lemmatize(token.lower()) for token in s1_tokens if not token.lower() in stopwords]
        s2_no_stopwords = [lemmatizer.lemmatize(token.lower()) for token in s2_tokens if not token.lower() in stopwords]
    else:
        s1_no_stopwords = [token.lower() for token in s1_tokens if not token.lower() in stopwords]
        s2_no_stopwords = [token.lower() for token in s2_tokens if not token.lower() in stopwords]

    s1_text = nltk.Text(s1_no_stopwords)
    s2_text = nltk.Text(s2_no_stopwords)

    s1_vocab = s1_text.vocab()
    s2_vocab = s2_text.vocab()

    s1_set = set(s1_vocab.keys())
    s2_set = set(s2_vocab.keys())

    union = s1_set.union(s2_set)

    s1_doc = [(s1_vocab[item] if item in s1_vocab.keys() else 0) for item in union]
    s2_doc = [(s2_vocab[item] if item in s2_vocab.keys() else 0) for item in union]


    if(similarityType == SimilarityType.EUCLIDEAN):
        return calculateEuclideanDistance(s1_doc, s2_doc)
    elif(similarityType == SimilarityType.JACCARD):
        return calculateJaccardDistance(s1_doc, s2_doc)
    else:
        return calculateManhattanDistance(s1_doc, s2_doc)

def compareLists(s1_val, s2_val):
    if  s1_val == s2_val:
        return s1_val, s1_val
    else:
        return 0, (s1_val + s2_val)


def calculateJaccardDistance(s1_doc, s2_doc):
    binary_s1_doc = [(1 if item > 0 else 0) for item in s1_doc]
    binary_s2_doc = [(1 if item > 0 else 0) for item in s2_doc]

    intersection = 0
    union = 0

    for i in range(len(s1_doc)):
        intersection_diff, union_diff = compareLists(binary_s1_doc[i], binary_s2_doc[i])
        intersection += intersection_diff
        union += union_diff

    jaccard_similarity = intersection/(union)
    return jaccard_similarity

def calculateManhattanDistance(s1_doc, s2_doc):
    manhattan_distance = 0
    for i in range(len(s1_doc)):
        manhattan_distance += abs(s1_doc[i] - s2_doc[i])
    
    return manhattan_distance

def calculateEuclideanDistance(s1_doc, s2_doc):
    
    distance_sum = 0
    for i in range(len(s1_doc)):
        distance_sum += (s1_doc[i] - s2_doc[i])**2
    
    euclidean_similarity = 1/(1 + math.sqrt((distance_sum)))
    return euclidean_similarity


# euclidean_similarity = similarity(emma, sense)
# jaccard_similarity = similarity(emma, sense, SimilarityType.JACCARD)
# manhattan_distance = similarity(emma, sense, SimilarityType.MANHATTAN)

# print(f"Euclidean similarity: {euclidean_similarity}")
# print(f"Jaccard similarity: {jaccard_similarity}")
# print(f"Manhattan distance: {manhattan_distance}")

# Stemming
'''
Stemming takes the common part of words so ends up with more words being the same than when no stemming happens
It is quicker than lemmatising the words
'''

# Lemmatising
'''
Lemmatising takes the base word from the dictionary
It takes longer as it has to be looked up
Only the words that have shorter words in the dictionary will be lemmatised - this causes problems with verbs as it defaults to assume it is a noun
This means that some of the words will stay the same as original when lemmatising - but not all
'''