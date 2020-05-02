x = 5 
if x==5:
    print('x jest równe 5')
else:
    print('x nie jest równe 5')    


#_________________

y = False

if y:
    print('prawda')
else:
    print('fałsz')    

#____________

z = 5 > 6

if z:
    print('prawda')
else:
    print('fałsz') 

#______________

j='1'
j='0'
j=''
j= False

if bool(j):
    print(1)
else:
    print(0)    

#_________________

k=input('Podaj k:')
if bool(k):
    print("Zmienna k zawiera dane")
else:
    print("Zmienna k nie zawiera danych")