arr = ['Genowefa', 'Onufry', 'Celestyna', 'Alojzy', 'Pankracy']
"""
a  = len(arr[0])
maincounter = []
for i in arr:
    if len(i) > a:
        print(i)
"""


long = len(arr[0])
zmienna = arr[0]

for i in arr:
    if(len(i)> long):
        long  = len(i)
        zmienna = i

print(zmienna)



