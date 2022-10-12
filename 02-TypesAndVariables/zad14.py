print("""
celsius - C
kelvin - K
fahrenheit - F
""")

C = float(input("Podaj temperature w celcjuszach: "))
K = (C + 273.15)
F = ((C * 1.8) + 32)
print(f'Temperatura dla C ={C}, w kelvinach wynosi{K}, a w fahrenheitah {F}')