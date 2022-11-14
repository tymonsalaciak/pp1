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