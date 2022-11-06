def f(number, even):
    if even == True:
        x = str(number)
        evensum = 0
        for i in x:
            if (int(i) % 2 == 0 ):
                #sum(int(i) for i in x)
                evensum = evensum + int(i)
        return evensum
    elif even == False:
        x = str(number)
        oddsum = 0
        for i in x:
            if (int(i) % 2 != 0 ):
                oddsum = oddsum + int(i)
        return oddsum



f(20576,False)