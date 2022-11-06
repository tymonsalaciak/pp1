def f(x):
    lenght = str(x)
    f = lenght[0]
    s = lenght[1]
    if f > s :
        return True
    elif s > f:
        return False



print(f(12122))