"""
26.	Write a program to find the second largest 
element in an array. Sample result:
Array: [5,1,9,6,1]
Result: 6
"""


arr = [5,1,9,6,1]

for i in arr:
    
    m = max(arr)
    mi = min(arr)
    if mi < i < m: #ten warunek sprawia że zostaje odrzucona największa wartość
        find = []
        find.append(i)
for j in find:
    end = max(find)
    print("Result:",end)
    # unikać używqania zmiennej end można pomylić z end=""
