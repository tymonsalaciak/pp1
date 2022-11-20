#Notatka dla mnie:

#  21:11 20.11.22 program ten prawdopodobnie można napisać wykonując operacje na 
# jednej liscie za pomocą funkcji 


"""
31.	Write a program to separate even and odd numbers
of a given array of integers. Put all even numbers first, and then odd numbers.
"""
#program ma odseparować parzyste od niep.. , najpierw mają być w liscie parzyste 


#ten draft rozdziela arr na listy parzyste i nieparz...
arr = [1,2,3,4,5,6,7,8,9,10,11,12,13]
arrODD = []
arrEVE = []
for i in arr:
    if i % 2 == 0:
        arrEVE.append(i)
        #arr.pop(i)
    else:
        arrODD.append(i)
        #arr.pop(i)

print(arrEVE)
print(arrODD)

#w tym momecie program dodaje na koniec arrODD do arrEVE

for i in arrODD:
    arrEVE.append(i)

print("po zmianach",arrEVE)
