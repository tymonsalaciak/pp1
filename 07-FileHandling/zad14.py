"""
14.	Write a program that calculates the number of lines for any text file. 
The user enters the name of the file from the keyboard. Display the result 
of the calculation (the file name and the number of lines). Do not display 
the contents of the file. Sample result:

File name: countries.txt
Number of lines: 14

"""

plik = input("add file to count lines: " )
x = 1
with open(plik, "r", encoding="utf-8") as f:
    print("File name:", plik)
    for line in f:  
        #print(x,line, end="") the file name and the number of lines
        x+=1
    print("Number of lines:",x-1) #dlaczego przy zapisaniu samego x wynik jest większy o 1 ???



#działa