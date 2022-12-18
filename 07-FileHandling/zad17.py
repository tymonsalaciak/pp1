""""
17.	Find any text file on the Internet and download it to your computer. 
Then write a program that copies the contents of this file to the copylines.txt file. 
Copy the contents of the file line by line. Finally, open both files in any text editor 
and check that their contents are the same.
"""


with open("poland.txt", "r", encoding="utf-8") as file:
    with open("copylines.txt", "a", encoding="utf-8") as copyline:
        for line in file:
            copyline.write(line)

