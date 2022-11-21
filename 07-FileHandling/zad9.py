file = open('numbers.txt','r',encoding="utf-8") 
sum = 0
for i in file:
    sum = sum +int(i)
    
print(sum)


