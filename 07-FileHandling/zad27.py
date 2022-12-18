#Then create a program that calculates the arithmetic mean of student’s grades.


import re

with open("grades.txt", "r", encoding="utf-8") as file:
    counter = []
    student_grades = file.read()
    grades = re.findall('\d.\d',student_grades) #zwraca liste
    for i in grades:
        i = float(i)
        counter.append(i)
    print(counter)
    

print(sum(counter)/ len(counter))

