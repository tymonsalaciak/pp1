"""39.	An array contains values:
 [[0,0,0,0,0],{0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]. 
 Create a program that modifies the array values
  to create a multiplication table as below. 
  Use loop statements. Display the array.
1  2  3  4  5
2  4  6  8 10
3  6  9 12 15
4  8 12 16 20
5 10 15 20 25

"""

arr = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

arr1 = [i +1 for i in arr]
for i in arr[0]:
        i = i + 1

print(arr1)


