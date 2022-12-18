



person = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming","excursions"],
    "married": True,
    "phone":{"landline":"123444321","mobile":"777888999"}
   }

for i in person:
    print(i)
print(person)
print("a :", person["name"])
print("b :", person["name"])
#tablica ma dane tego samgeo typu - jest niezmienna w czasie działania programu 
#60 min

#tablica asocjacyjna #mapa
print("c :", person["hobby"])
#print("b", person["name"])

person["married"] = False
print("e :", person["married"])

person["surname"] = "Nowak"
print("d :", person["surname"])

person["gender"] = "male"

print(person)

print("------")
#value()
x = person.get("hobby")
person["hobby"] += ["bicycle"]

print(person)

#x += ["bicycle"]
#print(x)

person["height"] = 1.88


person["phone"]["workphone"] = "123144" # tak jak w tablicach 2D aby dodać wartość do wewnętrzego
# słownika [][]
print(person)    