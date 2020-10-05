wordEntered = input("Enter a word with an affix")

affixes = ['pre', 'un', 'ality', 'ning', 'es']

for affix in affixes:
    lengthOfAffix = len(affix)
    word = ""
    if(wordEntered.endswith(affix)):
        word = wordEntered[:-lengthOfAffix]
        break
    elif (wordEntered.startswith(affix)):
        word = wordEntered[lengthOfAffix:]
        break
    else:
        word = wordEntered

print(word)