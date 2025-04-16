from collections import Counter
import re

def countwords(text):
    text = re.sub(r'[^\w\s]', '', text)
    word = text.split()
    word_count = Counter(word)
    return sum(word_count.values())
        

with open("coding-practice.txt" , 'r') as file:
    text = file.read().lower()
    lines = text.splitlines()
    print(f"There are {len(lines)} lines in this file")
    print(f"There are {countwords(text)} words in this file")
    print(f"There are {len(text)} characters in this file")





