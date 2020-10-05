import nltk

nltk.download('stopwords')
nltk.download('punkt')

from nltk.corpus import stopwords
from nltk import word_tokenize

text = "Dear diary, today I went to my first Computer Science lab where I learned about the natural language toolkit for Python"

text_tokens = word_tokenize(text)

# Lower case mans that tokens will math whatever their casing - we want this
tokens_without_stop_words = [word.lower() for word in text_tokens if not word in stopwords.words()]

print(tokens_without_stop_words)

filtered_sentence = (" ").join(tokens_without_stop_words)
print(filtered_sentence)

# Count occurrence counts
new_text = nltk.Text(tokens_without_stop_words)
print(new_text.count("science"))