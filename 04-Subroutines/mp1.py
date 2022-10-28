


#52|9031240001|9022

def card_number(x):
    lenght = str(x)
    p = lenght[0:2]
    k = lenght[12:16]
    masked = lenght[2:13]
    print(f'{p}************{k}')

    

  

card_number(5290312400019022)


"""    i =  x[2:13] 
    p = x[0:2]
    k = x[13:15]
    while p> i > k:
        print(f'{p}{i}{k}')
        break"""