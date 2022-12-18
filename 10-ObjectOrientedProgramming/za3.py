
"""k = 'uniwersytet'
print(k[3:8])

z =str(9 + 9) + "9 + 9" + str(9) + str(9)

print(z)

y = 'to be or not to be'
x = y[0b11:0xB] #be or no  # [3:11]
print(x)
str(9 + 9) + "9 + 9" + str(9) + str(9)



print(f"items - tuple {d.items()}")
print(f"keys {d.keys()}")
print(f"values {d.values()}")


for key in d.keys():
    print(f"key; {key}  value; {d[key]}")

for val in d.values():
    print(val)


d = dict(pet="dog", age=45, name="spot", color ="black", size = "tiniy")
print(d)

#for key,val in d.items(): wyswietla wszystko
   # print(key,val)

for key in d.keys():
    print(key) #zwróci klucze                  # d[key] - zwróci wartosci 

for val in d.values():
    print(val)




x = 4
for i in range(5): # 5 nie wchodzi 0-4
    if i % 2 == 0:
        continue
    x += 1

print(x)

k = 'uniwersytet'
print(k[3:8])

z =str(9 + 9) + "9 + 9" + str(9) + str(9)

print(z)

y = 'to be or not to be'
x = y[0b11:0xB] #be or no  # [3:11]
print(x)
"""

print(0x9 % 0b11 + 9) # = 9
#print(10 & 1)
print(9 % 3 + 9)
import re

x = "1.22.333.4444.55555.666666"
pattern = "\d+"
c = re.findall(pattern,x)
print(len(c))