#the first name, last name and email address of students under 30

import csv

with open("students.txt", "r", encoding="utf-8") as fcsv:
    reader = csv.DictReader(fcsv)
    for i in reader:
        if int(i['age']) < 30:
            print(i['first_name'], i['last_name'], i['email']) 

"""

def f(age):
    with open("students.txt", "r", encoding="utf-8") as fcsv:
        read = csv.DictReader(fcsv)
        for i in read:
            if int(i["age"]) <= age:
                x = f""{i["first_name"]},{i["last_name"]}, {i["email"]}
    return x

f(30)
"""



import re 

text = "zosoosma  16 dasfa 2 114 faff yuuaaaa 10024 , 8"
pattern = re.compile(r"\d+")

arr= []
result = re.findall(pattern,text)
print(result)
for i in result:

    if 2 <= len(i) <= 3:
        i = int(i)
        arr.append(i)

    x = sum(arr)

print(x)












"""
arr =[]
for s in text:
    if int(s) % 2 ==0:
        
            arr.append(int(s))

            print(result)
sum = 0
for i in result:
    i = int(i)
    if i % 2 ==0:
        sum += i
    else:
        pass
print(sum)
"""