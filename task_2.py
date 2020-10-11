# import libraries
from pprint import pprint
from collections import Counter
import xml.etree.ElementTree as ET

# function return top 10 words
def get_xml_top(filename):
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
    for i in lst:
        if len(i) >= 6:
            total_lst.append(i)

    # count how many times the word appears in the text
    cap_words = [word.upper() for word in total_lst]
    word_counts = Counter(cap_words)
    # create a list
    result = []
    for k, v in word_counts.items():
        result.append([k, v])
    # Sorted by value
    result = sorted(result, key=lambda x: x[1], reverse=True)
    # Create top 10
    top_10 = result[:11]
    return top_10

pprint(get_xml_top("newsafr2.xml"))
