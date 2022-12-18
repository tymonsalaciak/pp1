"""
writes 50 random integers between 100 and 999 to a text file
"""

import random 

with open("file19.txt", "a", encoding="utf-8") as file:
    for i in range(1,51):
        z = random.randint(100,999)
        e = str(z)
        file.write(f'{e}\n')