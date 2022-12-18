"""
16.	Find any text file on the Internet and download it to your computer. 
Then write a program that copies the contents of this file to the copy.txt file. 
Copy the contents of the file as a whole. Finally, open both files in any text 
editor and check that their contents are the same.

import shutil

shutil.copyfile('poland.txt', 'copy.txt')

in_origin =  open('poland.txt', 'r', encoding='utf-8')
print(in_origin.read())
print("------------")

in_copy =  open('copy.txt', 'r', encoding='utf-8')
print(in_copy.read())
"""
#1 otwarcie pliku
#2 odczyt pliku 
#3 wpisanie pliku 
#4 zamkniecie 

with open('poland.txt', "r") as file:
    content = file.read()
    with open('polandcopy.txt', 'a') as copy: # a - append() mode co zostanie dodane do pliku   
        copy.write(content) # ma wpisać to co zostało odczytane file.read()

"""
.write()
.read()
open()
"""

    
