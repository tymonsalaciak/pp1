import json
# read zwraca cią znakowy
# tablica słowników na kolokwium zad 8-10
#
with open("data.json") as file:
    data = json.load(file)

for i in data:
    for k,v in i.items():
        print(k,":",v)
