a = input("Podaj liczbę a:")
b = input("Podaj liczbę b:")
c = input("Podaj liczbę c:")

a = float(a)
b = float(b)
c = float(c)

if c > 0:
    wynik = (a * a) + b
elif c < 0:
    wynik = a - (b * b)
else:
    if a-b == 0:
        wynik = "Proba dzielenia przez 0"
    else:
        wynik = 2/(a-b)

print("Wynik to " + str(wynik))    