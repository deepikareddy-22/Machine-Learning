import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter

# Download required resources (run once)
nltk.download('punkt')
nltk.download('stopwords')

# Sample text
text = "Natural Language Processing helps computers understand human language."

# 1. Tokenization
tokens = word_tokenize(text.lower())

# 2. Remove stopwords
stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word.isalnum() and word not in stop_words]

# 3. Word frequency
word_freq = Counter(filtered_tokens)

# Output
print("Tokens:", tokens)
print("Filtered Tokens:", filtered_tokens)
print("Word Frequency:", word_freq)
