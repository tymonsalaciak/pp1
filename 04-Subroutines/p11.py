def f(n):
    ciag = ""
    for i in range(1,n+1):
        i = str(i)
        ciag = ciag+i
    return ciag

print(f(11))