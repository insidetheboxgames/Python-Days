# day 1 - 30 day challenge: Regular Expressions

import re
from collections import Counter

# Have to be exactly the same
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
words = re.findall(r'\w+', paragraph)
word_count = Counter(words)
print(word_count)

points = ['-12', '-4', '-3', '0', '-2', '4', '10']
points = sorted(points)
distance = int(points[0]) - int(points[len(points)-1])
print(distance)

def is_valid_variable(str):
    regex_pattern1 = r'[A-Za-z0-9]|_'
    regex_pattern2 = r'^\d'
    matches = re.findall(regex_pattern2, str)
    if len(matches) != 0:
        return False
    else:
        matches = re.findall(regex_pattern1, str)
        if len(matches) == len(str):
            return True
        else:
            return False
        
print(is_valid_variable('firstname'))
print(is_valid_variable('first-name'))
print(is_valid_variable('first_name'))
print(is_valid_variable('2name'))
