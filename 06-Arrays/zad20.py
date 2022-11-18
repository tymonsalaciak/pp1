"""
20.	An array contains integer numbers: 12, 6, 4, 9, 10. Create a program that 
displays the array values graphically as below. Define a function star(n) that
returns the given number of asterisks as a string. Use a defined function in the program.

12: ************
 6: ******
 4: ****
 9: *********
10: **********

gdy coś poszło nie tak
arra = ['*'* i for i in arr]
for i in arra:
    print(i)

"""
arr =[12, 6, 4, 9, 10]
#stworzyłem kolejną tablice która zamianiła mi i na irazy *, potem wydrukowałem to co w niuej było 

arra = ['*'* i for i in arr]

#nie zwraca cyfr zawartych w arr
for i in arra:
    print(f":{i}")

#print(arra)

print("_______________")

#rozwiącanie, kluczowe było miejsce w którym znajduje sie print  
for i in arr:
    x = "*" * i
    print(f"{i}: {x}")

