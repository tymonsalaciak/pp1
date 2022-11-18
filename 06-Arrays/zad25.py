"""
25.	Define a function occurs(number, array) that returns True if a 
given number is present in an array. Then create a program that checks 
whether the number entered from the keyboard is present in the array [15, 38, 7, 23, 14]. Sample result:
Number: 23
Array: 15 38 7 23 14
Result: number 23 appears in the array


"""



def occurs(num, arr):
    if num in arr:
        return True

data = [15, 38, 7, 23, 14]

print(occurs(23,data))



def occurs(num,arr):
    num = int(input("Number:" ))
    if num in arr:
        return True
    else:
        return False

data = [15, 38, 7, 23, 14]

print(occurs(0,data))