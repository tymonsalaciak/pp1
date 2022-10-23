"""print("podaj ilość godzin przepracowanych - h ")
print("podaj stawkę godzinową - p ")
"""
def computepay(h, p):
    Wynagrodzenie = h*p
    premia = 1.5 * Wynagrodzenie
    if h > 40:
        print(premia)
    elif h <= 40:
        print(Wynagrodzenie)


computepay(255, 78)