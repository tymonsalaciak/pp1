

arr = [[True,False],[True,True],[False,False]]

for i in arr:
    for j in i:
        if j == True:
            j = False
        else:
            j = True 
        print(arr)

