slownik = {'key1' : 'value1', 'key2' : 'value2'}

pracownik = {'imie':'Jan', 'nazwisko':'Kowalski', 'wiek':30,
 'miasto': 'poznan', 'imionaDzieci': ['Adam', 'Ewa'], 
 'imionaRodzicow': ['Paweł', 'Julia'] }

print(pracownik)

pracownik['wzrost'] = 175
print(pracownik)

#________

pracownik1 = {
    'name':'Anna',
    'surname':'Kowalska',
    'city':'Poznan',
    'age': 24 
}
print()
print(pracownik1)

key = 'age'
if key in pracownik1:
    del pracownik1[key]
    print(f'Klucz {key} zostal usuniety')
else:
    print(f'Klucz {key} nie zostal usuniety')  

print(pracownik1)  
print(pracownik1.keys())
print(pracownik1.values())

print(list(pracownik1.values()))
print(pracownik1.items())

for value in pracownik1.values():
    print(value, end=" ")
print()    

for key, value in pracownik1.items():
    print(f'{key}: {value}')

