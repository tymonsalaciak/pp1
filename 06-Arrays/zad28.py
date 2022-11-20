def median(arr):
    leng = len(arr) 
    x = leng // 2 
    if leng % 2 == 0:
        mid1 = arr[x-1]
        mid2 = arr[x]
        mediana = (mid1 + mid2) /2
        return mediana
    else:
        mid2 = arr[x]
        return mid2

        


arr1 = [1,0,9,4,6,] # 9
arr2 = [6,8,3,1,0,5,7] # 1
arr3 = [6,8,3,4,3,5,7,3] # 3.5


print("mediana:",median(arr1))
print("mediana:",median(arr2))
print("mediana:",median(arr3))


"""
leng = len(arr3) 
x = leng // 2 
print(f'ma dłufosc: {leng}, mid: {x}')
mid1 = arr3[x-1]
print(mid1)
mid2 = arr3[x]
print(mid2)
mediana = (mid1 + mid2) /2
print(mediana)

#print(len(arr1))

#zwraca mediane nieparzystej ilosci
leng = len(arr1) 
x = leng // 2 
print(arr1[x])

"""


