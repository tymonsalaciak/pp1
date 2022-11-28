"""
8.	Create a dictionary as in the example below. Note the structure of 
the dictionary (key-value) and the value types in the example below. 
What type of value was used in each of the six key-value pairs?


Then, create a program and do the following tasks:
a.	Display contents of the dictionary
b.	Display name
c.	Display hobby
d.	Change surname to Nowak
e.	Change person's marriage status
f.	Add gender: male
g.	Add a new hobby: bicycle
h.	Add work phone to existing phones: 313131444

"""


from re import X


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