"""22.	Two arrays contain the following integer numbers [4,36,12,28,9,44,5] and [5,1,36]. 
Create a program that displays the numbers from the first array that do not appear in the second array.



for i in arr2:
    cleAr = arr1.pop(i)

print(arr1)


#odejmowanie elemntów z jednej tablicy nie bedzie możliwe ponieważ 
# może nie posiadać takiej liczby jaka ma ta pierwsza w tym przypadku 1

arr1 = [4,36,12,28,9,44,5]
arr2 = [5,1,36]
for j in arr2:
    for i in arr1:
        if i == j : 
            cleAr = arr1.pop(i)
        else:
            pass

print(arr1)

for x in arr1 and for y in arr2:

"""
arr1 = [4,36,12,28,9,44,5]
arr2 = [5,1,36]

arr3 = [x for x in arr1 if x not in arr2]

print(arr3)