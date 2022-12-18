"""
Then write a program that displays all words with at least six letters from the file. 
Display each word on a separate line. Use regular expressions.
"""

import re

with open("poland.txt", "r", encoding="utf-8") as file:
    text = file.read()
    words = re.findall('[a-zA-z]{6,}',text) # [a-zA-z]{6,}' zwraca liste {6}-tylko 6  {,6} - mniej niż 6
    for i in words:
        print(i)