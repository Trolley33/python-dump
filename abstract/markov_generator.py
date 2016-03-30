import sys
import re
from pprint import pprint
from random import choice
 
EOS = ['.', '?', '!']
 
 
def build_dict(words):
    """
    Build a dictionary from the words.
 
    (word1, word2) => [w1, w2, ...]  # key: tuple; value: list
    """
    d = {}
    for i, word in enumerate(words):
        try:
            first, second, third = words[i], words[i+1], words[i+2]
        except IndexError:
            break
        key = (first, second)
        if key not in d:
            d[key] = []
        #
        d[key].append(third)
 
    return d
 
 
def generate_sentence(d):
    li = [key for key in d.keys() if key[0][0].isupper()]
    key = choice(li)
 
    li = []
    first, second = key
    li.append(first)
    li.append(second)
    while True:
        try:
            third = choice(d[key])
        except KeyError:
            print("END ON {}".format(key))
            break
        li.append(third)
        if third[-1] in EOS:
            break
        # else
        key = (second, third)
        first, second = key
 
    return ' '.join(li)
 
 
def main():
    file_name = input("Enter file name: ")
    try:
        with open(file_name, "rt", encoding="utf-8") as f:
            text = f.read()

        words = text.split()
        # Remove timestamps
        words = [re.sub(r"[0-9][0-9]:[0-9][0-9]", ' ', x) for x in words]
        # Remove datestamps
        words = [re.sub(r"[0-9][0-9] [A-Za-z]", '\n', x) for x in words]
        d = build_dict(words)
        sent = generate_sentence(d)
        while sent in text:
            sent = generate_sentence(d)
        print(sent)
    except (OSError, IOError):
        print("Invalid file name.")

main()
input()