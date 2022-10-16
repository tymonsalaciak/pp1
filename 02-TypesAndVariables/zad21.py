import random

szukanaLiczba = random.randrange(1,6)

zgadywanaLiczba = 0

while zgadywanaLiczba != szukanaLiczba :
    zgadywanaLiczba = int(input("podaj liczbę: "))
    if (zgadywanaLiczba < szukanaLiczba):
            print("za mała liczba oczek")
    elif (zgadywanaLiczba > szukanaLiczba ):
        print("za duża liczba oczek")
    else:
        print(True)



