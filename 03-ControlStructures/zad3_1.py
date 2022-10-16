"""
Podaj liczbe godzin: 45
Podaj stawke godzinowa: 10
Wynagrodzenie: 475.0


t = 
h = int(input("podaj ilość godzin przepracowanych:")) 
"""

h = int(input("podaj ilość godzin przepracowanych:")) 
p = float(input("podaj stawkę godzinową:"))
Wynagrodzenie = h*p

#print(Wynagrodzenie)

premia = 1.5 * Wynagrodzenie

print(premia)

if h > 40:
    print(premia)
elif h <= 40:
    print(Wynagrodzenie)
