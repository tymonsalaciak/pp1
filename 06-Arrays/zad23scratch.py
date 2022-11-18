"""
array = [-2, 45, 0, 11, -9]

for i in range(len(array)):
    #print(i)# 0-4
    for j in range(0, len(array) - i - 1):
        print(j)
       
0 
1       -1 pozycje indexu
2
3

0
1       -2
2

0       -3
1

0       -4
        """


"""

def bubblesort(arr):
    for i in range(len(arr)):
        for j in range(0,len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                asc = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = asc


data = [9, 6, 8, -90, -4, -2134, 99, 65]

bubblesort(data)
print(data)
"""

arr1 = [2, 3, 2, 5, 8, 1, 9, 8]


for i in arr1:
    if arr1.count(i) == 1:
        end = []
        end.append(i)
print(end)





print(arr1)