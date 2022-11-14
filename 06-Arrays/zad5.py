import random



arr3 = [7 for i in range(5)]
arr4 = [i for i in range(1,10)]
arr5 = [i*2 for i in range(1,10)]

arr6 = [random.randint(1,20) for i in range(10)]
#arr7 = [[] for i in range(5)]
arr7 = [[2 for i in range(3)] for i in range(5)]
#arr7 = [2 for i in range(5)]
arr8 = [[1 for i in range(2)] for j in range(4)]
arr9 = [[random.randint(1,20) for i in range(3)] for j in range(5)]


print(arr3)
print(arr4)
print(arr5)

print(arr6)
print(arr7)
print(arr8)
print(arr9)
