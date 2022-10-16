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
    c, k = min(x), max(x)
print(f'wpisałeś łącznie: {ilosc}')
print(f'ich suma wynosi: {suma}')
print(f'najmniejsza liczba to{c}, a największa to {mk}')