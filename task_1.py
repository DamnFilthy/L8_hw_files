# import libraries
import json
from pprint import pprint
from collections import Counter

def get_json_top(filename, char, rating):
    # Reading
    with open(filename, encoding='utf-8') as f:
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
        if len(word) >= char:
            total_lst.append(word)

    # count how many times the word appears in the text
    cap_words = [word.upper() for word in total_lst]
    word_counts = Counter(cap_words)
    # create a list
    result = []
    for key, value in word_counts.items():
        result.append([key, value])
    # Sorted by value
    result = sorted(result, key=lambda x: x[1], reverse=True)
    # Create top 10
    top_words = result[ : rating + 1]

    return top_words

pprint(get_json_top("newsafr1.json" , 6, 10))
