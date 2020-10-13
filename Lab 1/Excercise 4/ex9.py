words = ["This", "is", "a", "word", "list"]

print("Sorted: " + sorted(words))
print("Original: " + words)
words.sort()
print("Original: " + words)

# sorted(words) prints does not change the order of the original list
# words.sort() changes the original order of the list