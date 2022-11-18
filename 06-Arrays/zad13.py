li = [[3,9,2],[2,4,5],[7,1,6],[0,4,8]]

sum = 0

for i in li:
    for j in i:
        if j % 2 == 0 :
            sum = sum + j
        else:
            pass
# miejsce w którym umiescisz print(sum) jest kluczowe
print(sum)        
