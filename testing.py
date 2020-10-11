# import libraries
import json
from pprint import pprint
from collections import Counter


# Reading
with open("newsafr1.json", encoding='utf-8') as f:
    file = json.load(f)
    # Empty string
    all_words = ''
    titles = file["rss"]["channel"]["items"]
    # One big string
    for title in titles:
        all_words = all_words + ' ' + title["description"]

# List of words
lst = all_words.split()

# List where word bigger than 6 char
total_lst = []
for word in lst:
    if len(word) >= 6:
        total_lst.append(word)

# count how many times the word appears in the text
cap_words = [word.upper() for word in total_lst]
# word_counts = Counter(cap_words)
word_counts = Counter(cap_words).most_common(10)
pprint(word_counts)
