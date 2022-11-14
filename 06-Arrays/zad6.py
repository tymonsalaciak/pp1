<<<<<<< HEAD
arr = [2, 3, 7, 5, 4]

print(arr)
print(len(arr))
print(arr[0])
print(arr[1])
print(arr[-1])
s = arr[0] + arr[-1]
print(f'sum of the first and last value {s}')
print(arr[2])

#(x, end=" ")
separated = [(i ," ") for i in arr ]
print(separated)

first = [i for i in arr[0:3]]
print(first)
=======
import array as arr

arr = [2, 3, 7, 5, 4]

print(arr[-1])

for i in arr:
    print(i, end=" ")

#zmiena przechowuje jedną wartosc
#arr - tablice 
# kontener przechowujący wiele wartosci 
# tablica przechowuje dane jednego typu 
# lista różnych 
# tablica jest niezmiena od poczatku do konca programu 
# numpy należy zaimportować i pobrać 
# zajżecz co ma w sobie numpy

# w g można wykożystać % 
# mid

print("j")
for i in range(0, int(len(arr)/2) + 1 ):
    print(arr[i], end=" ")
>>>>>>> edfd847231b49f96668d1eeba08fb174fb866bfe
