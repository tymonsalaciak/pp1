#try i except,
"""
h = int(input("podaj ilość godzin przepracowanych:")) 
p = float(input("podaj stawkę godzinową:"))
Wynagrodzenie = h*p

#print(Wynagrodzenie)

premia = 1.5 * Wynagrodzenie

print(premia)
"""
try:
    h = int(input("podaj ilość godzin przepracowanych:")) 
    p = float(input("podaj stawkę godzinową:"))
    Wynagrodzenie = h*p
    premia = 1.5 * Wynagrodzenie
    if h > 40:
        print(premia)
    elif h <= 40:
        print(Wynagrodzenie)
except:
    print("podaj wartość numeryczną!")
#continue