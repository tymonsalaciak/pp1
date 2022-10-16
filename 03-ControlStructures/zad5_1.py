"""
    count = 0
for itervar in [9, 41, 12, 3, 74, 15]:
    count = count + 1
    print('Ile:', count)

    try 

except
"""

ilosc = 0
suma = 0
while True:
    zbior = input("podaj liczbę: ")
    if zbior == "gotowe":
        break
    try: 
        x = int(zbior)
    except:
        print("podaj tylko liczby nie słowa ")
        continue
    ilosc += 1
    suma += x
    srednia = suma/ilosc
print(f'wpisałeś łącznie: {ilosc}')
print(f'ich suma wynosi: {suma}')
print(f'a ich średnia jest równa: {srednia}')