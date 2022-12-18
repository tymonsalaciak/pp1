import re

text = "To be, or not to be, that is the question"
vowels = re.findall(r'\w+',text) # \'w+'
print(vowels)
print(len(vowels))



m = re.split(" ",text)
print(m)
print(len(m))