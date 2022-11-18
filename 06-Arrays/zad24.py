"""
Array: 2 3 2 5 8 1 9 8
Unique elements:


"""
def Uniqe(arr):
    licz = []
    mlist = list(arr)
    for i in mlist:
        x = mlist.count(i)
        if x >= 2:
            licz.append(i)
    print(licz)
    end = [x for x in arr if x not in licz]
    print(end)
    return end
    

arr1 = [2, 3, 2, 5, 8, 1, 9, 8]

print(Uniqe(arr1))




"""

Uniqe(arr1)
print(arr1)
arr1 = [2, 3, 2, 5, 8, 1, 9, 8]

end = [arr1.pop(i) for i in arr1 if i in arr1.count(i)> 1]



print(end)
"""