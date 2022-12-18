"""
19.	Create a program that writes to a text file integer numbers 
in the range of <1,50>, every number in a separate line
"""

with open("file19.txt", "a", encoding="utf-8") as file:
    for i in range(1,51):
        e = str(i)
        file.write(f'{e}\n')