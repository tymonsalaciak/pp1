letters = {"a" :  "Alfa",
"b" : "Bravo",
"c" : "Charlie",
"D" : "Delta",
"E" : "Echo",
"F" : "Foxtrot",
"G" : "Golf",
"H" : "Hotel",
"I" : "India",
"J" : "Juliett",
"K ": "Kilo",
"L" : "Lima",
"M" : "Mike​",
"​N" : "November",
"O" : "Oscar",
"P" : "Papa",
"Q" :"Quebec",
"R" :"Romeo",
"S" : "Sierra",
"T"  :"Tango",
"U": "Uniform",
"V" : "Victor",
"W" : "Whiskey",
"X" : "X-ray",
"Y": "Yankee",
"Z" : "Zulu"}

import json
"""
lista = []

x = input("give leters: ")
with open("icao.json", "r") as in_json:
    icao = json.load(in_json)

for i in x:
    for i in letters:
        lista.append(i)





"""
x = input("give leters: ")

lista = []

for i in x.upper():

    lista.append(letters[i])
    
# na ten momęt działa całkiem prymitywnie 

#spróbuje by program pobierał litery i niezależnie od tego jakie się poda zwracał pobrane stringi z pliku json
for icao in lista:
    print(icao, end=" ")

