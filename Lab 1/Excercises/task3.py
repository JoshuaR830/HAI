import nltk

from nltk import word_tokenize
from nltk import pos_tag

prefix = "../../../Text Doc Collection/"

nounCountList = []
verbCountList = []
adjectivesCountList = []

def tagFileContent(text):
    tokens = word_tokenize(text)
    tags = pos_tag(tokens, tagset='universal')
    return tags

def processFile(file):
    text = ""
    for line in file:
        text += line
    return text

for x in range(1, 5):
    with open(prefix + "text" + str(x) + ".txt", encoding="utf8") as file:
        fileContent = processFile(file)
        tags = tagFileContent(fileContent)

        adjectivesCountList.append(sum(1 for value in tags if value[1] == "ADJ"))
        verbCountList.append(sum(1 for value in tags if value[1] == "VERB"))
        nounCountList.append(sum(1 for value in tags if value[1] == "NOUN"))

        adjectiveCount = sum(adjectivesCountList)
        verbCount = sum(verbCountList)
        nounCount = sum(nounCountList)

        total = adjectiveCount + verbCount + nounCount

print(f"Adjectives: {(adjectiveCount/total)*100}%")
print(f"Verbs: {(verbCount/total)*100}%")
print(f"Nouns: {(nounCount/total)*100}%")

print(f"{adjectiveCount}:{verbCount}:{nounCount}")