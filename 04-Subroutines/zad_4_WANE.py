import math
#dir(math)

math.pi
def volume(r):
    v = (4.0/3.0) * math.pi * r**3
    return v

print(volume(30))