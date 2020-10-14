import nltk
import task1

emma = nltk.corpus.gutenberg.raw('austen-emma.txt')
sense = nltk.corpus.gutenberg.raw('austen-sense.txt')
persuasion = nltk.corpus.gutenberg.raw('austen-persuasion.txt')
bible = nltk.corpus.gutenberg.raw('bible-kjv.txt')

documents = [emma, sense, persuasion, bible]

docCount = len(documents)

matrix = [[0 for i in range(docCount)] for j in range(docCount)]

for i in range (docCount):
    for j in range (docCount):
        matrix[i][j] = task1.similarity(documents[i], documents[j])

seperator = "+--------"
seperator_line = ""

for a in range(len(documents)):
    seperator_line += seperator 
seperator_line += "+"

print("   ", end="")
for x in range(len(documents)):
    print(f"|   d{x}   ", end="")

print("|")

count = 0
for y in matrix:
    print("   "+seperator_line)
    count += 1
    print(end=f"d{count} |")
    for x in y:
        print("%2f" % x, end="|")
    print()

print("   " + seperator_line)