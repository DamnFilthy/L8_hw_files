# import libraries
from pprint import pprint
from collections import Counter
import xml.etree.ElementTree as ET

# function return top 10 words
def get_xml_top(filename, char, rating):
    parser = ET.XMLParser(encoding = "utf-8")
    tree = ET.parse(filename, parser)
    root = tree.getroot()
    # Make string of text
    items = root.findall("channel/item")
    all_words = ''
    for item in items:
        all_words = all_words + ' ' + item.find("title").text

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
    top = result[ : rating + 1]
    return top

pprint(get_xml_top("newsafr2.xml", 6, 10))
