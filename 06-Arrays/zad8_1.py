arr = [-15, 8, -31, 47, -2, 19]

#print(min(arr))
#print(max(arr))


max = arr[0]
minn = arr[0]


for x in arr:
    if(x >max):
        max = x 
    if(x < minn ):
        max= x


print(minn, max)



""" 
a = arr[2]

for i in arr:
    if i > a:
        print(i)


for i in arr:
    if i <= a:
        print(i)
"""