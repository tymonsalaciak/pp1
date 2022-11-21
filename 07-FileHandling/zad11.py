arr = ['star wars' ,'cube' ,'red' ,'pulp fiction' ,'4 roums' ]
file = open('title.txt','w',encoding="utf-8")
for i in arr:
    file.write(i)
    file.write("\n")

file.close()