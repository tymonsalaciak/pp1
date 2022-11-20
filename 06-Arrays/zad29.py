"""
29.	Write a program that, for the given array of real numbers, 
displays the number of elements that are greater than the given value entered from the keyboard.
"""
#import random 
t = float(input("given value:"))
arr = [1, 3.5, 5,66.99, 44.5] #
#rand = random.random()
arr.append(t)
print(arr)


#displays the number of elements that are greater than the given

for i in arr:
    sum = 0
    if i > t: #opcjonalnie >=
        #values = arr.count(i)
        sum = 1 + sum
        print("number graetaer than value t ",i)
        print(sum)
    else:
        pass

    




'''
for t in arr:
    if 
    print(z)

for  i in arr:
    if t > arr[i]:
        print(t)
else:
    pass'''