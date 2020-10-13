from nltk.corpus import stopwords

print(stopwords.words('English'))

# Problems with a fixed stopword list
# You could remove some context that is only inferred through use of stopwords - e.g. who I, my, ours, yours

# Not really sure

# Internet search time
# The group of words may be different in different scenarios
# Problems when searching if phrases include them
# Problems with names such as "The Who", "Take That"

# Helps to save space in database
# Helps to reduce processing large amounts of data



# Overcoming these challenges
# I don't know
# You could have a phrases list - but that is just adding complexity to the problem
# You could make it case sensitive - but to lower case to ensure tokens match will stop that - so not helpful