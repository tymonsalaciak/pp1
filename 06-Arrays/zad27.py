"""
27.	Write a program that displays the difference between 
the largest and smallest values in an array of integers. 
Sample result:
Array: [5,1,9,6,1]
Result: 8
"""

arr = [5,1,9,6,1]
m = max(arr)
mi = min(arr)
x = m - mi 
print("Result:",x)