arr = [[0,0,0],[0,0,0],[0,0,0]]
#          0        1       2

#9:31 15.11.22 Dobra robota
for i in arr:
    arr[0][0] = 1
    arr[1][1] = 1
    arr[2][2] = 1

for i in arr:
    for j in arr[0]:
        if  i == arr[0]:
            print(j, end=" ")
    print(end="\n")
    for j in arr[1]:
        if  i == arr[0]:
            print(j, end=" ")
    print(end="\n")
    for j in arr[2]:
        if  i == arr[0]:
            print(j, end=" ")
            
            

    

  



"""
for i in arr:
  #print(i)



for i in range(1,10):
    if i <= 3:
        print(f"{i}", end="\n")
    elif i <= 6:
        print(f"{i}" , end=' ')
    elif i <= 9:
        print(f"{i}" , end='\n')
"""