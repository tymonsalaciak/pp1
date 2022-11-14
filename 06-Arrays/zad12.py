import array  as li
#a
li = [
    [2,5,4],[9,0,3]
    ]
print(li)
#b
print(len(li))
for i in li:
    print(len(i))
# zerowy element zwnętrnej tablicy i dry element wewnetrznej tablicy 
print("wyniki")
#print(li[1][1])
print(li[1][0])
#print(li[1][1])

for i in li:
    for z in i:
        print()