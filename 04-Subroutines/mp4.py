"""f(3124,True) => 6
f(3124,False) => 4"""


def sumnumber(number, even):
    evensum = 0
    oddsum = 0
    string1 = str(number)
    for i in range(0, len(string1)+1):# tutaj może być błąd
            if even == True and (i % 2) == 0: 
                evensum = evensum + i # dotąd działa
            elif even == False and i != i%2: # przyjżeć się warunkom
                oddsum = oddsum + i

    print("sum of even numbers is:",evensum)
    print("sum of even odd is:",oddsum)


sumnumber(20576,False)

"""
        elif even == :
            oddsum = oddsum + i
            print("sum of even numbers is:",evensum)
        print(oddsum)"""
#if (i % 2 != 0):
