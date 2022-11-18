"""
Array: 8 2 5 1 9
2nd power: 64 4 25 1 81

"""

arr = [8, 2, 5, 1, 9]

#w pierwszej częci należy umiecic operacja jaką chcę wykonać

arr2nd = [i ** 2 for i in arr]

print(arr2nd)