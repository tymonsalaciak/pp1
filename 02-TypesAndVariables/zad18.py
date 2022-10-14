import math

a,b,c = 3,4,5

p = 0.5*(a + b + c)
H = p*(p-a)*(p-b)*(p-c)

print(math.sqrt(H))
