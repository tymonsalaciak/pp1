"""
Wartosc Ocena
>= 0.9 5,0
>= 0.8 4,5
>= 0.7 4,0
>= 0.6 3,5
>= 0.5 3,0
< 0.5 2,0
Podaj wartosc: 0.95 = 5.0

while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'zrobione':
        break




"""
#if 0.0 <= x and x <= 1.0:
x = float(input("podaj wartość od 0.0 - 1.0, aby uzyskać wynik: "))
try:
    while True:
        if 0.0 <= x and x <= 1.0:
            if  x >= 0.9:
                print("5,0")
            elif  x >= 0.8:
                print("4,5") 
            elif  x >= 0.7:
                print("4,0")
            elif  x >= 0.6:
                print("3,5")
            elif  x >= 0.5:
                print("3,0")
            elif  x < 0.5:
                print("2,0")
            break
except:
    print("podaj tylko liczby nie słowa ")
    continue