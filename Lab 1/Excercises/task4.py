# Given string s
# Given a number n
# Return the top n tokens (words) by decreasing frequency

# Should use the vocab() method of a text object
# Gives text in form of a dictionary
# Key is the token
# Value is number of occurrences
def topN(s, n):
    freq = s.vocab()
    print(freq)


sentence = "If Peter Piper picked a peck of pickled peppers, how many pickled peppers did Peter Piper pick"

topN(sentence, 3)