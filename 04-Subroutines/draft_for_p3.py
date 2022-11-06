def f(amount):
    x = amount // 5 # tu jest 4
    s1 = amount - x * 5
    if (s1 == 2):
        s = 1 
        return s
    else:
        y = s1 // 2  # ma być 1
        z = y //1 
        whole = x+y+z
        return whole

print(f(2))


'''
def f(amount):
    x = amount // 5 # tu jest 4
    s1 = amount - x * 5
    #wykorzystać if dla przypadku 2 == 2
    y = s1 // 2  # ma być 1
    z = y //1 
    whole = x+y+z
    return whole

f(2)
'''