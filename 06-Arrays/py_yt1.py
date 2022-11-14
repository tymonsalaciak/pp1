A = [1, 3, 5, 7]
B = [2, 4, 6, 8]
C = [9, 10, 13, 45]

possibilities = [(a, b, c) for  a in A for b in B for c in C]

print(possibilities)