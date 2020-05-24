liczbaElementow = 0
while(True):
    liczbaElementow = input("Podaj liczbę wprowadzanych elementów do posortowania <1 .. 10>")

    if int(liczbaElementow) < 0: 
       print("Zła liczba spróbuj ponownie...") 
    else:
        break

print("Podaj liczby")

tablica = []

for i in range(int(liczbaElementow)):
    tablica.append(input("Wprowadź liczbę [" + str(i + 1) + "]: "))

print("Wprowadzanie posortowanych elementów")
tablica.sort()
new = sorted(tablica)
for x in new:
    print(x)



