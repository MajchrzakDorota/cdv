imie1 = input('Podaj imie')
nazwisko1 = input('Podaj nazwisko')
wiek1 = input('Podaj wiek')

imie2 = input('Podaj imie')
nazwisko2 = input('Podaj nazwisko')
wiek2 = input('Podaj wiek')

user1= {
    'Imię': imie1,
    'Nazwisko': nazwisko1,
    'Wiek': wiek1
}

user2= {
    'Imię': imie2,
    'Nazwisko': nazwisko2,
    'Wiek': wiek2

}

for key, value in user1.items():
    print(f'{key}: {value}')

for key, value in user2.items():
    print(f'{key}: {value}')    

wiek3 = (int(wiek1) + int(wiek2))/2

print('Średni wiek użytkowników wynosi: '+ str(wiek3))