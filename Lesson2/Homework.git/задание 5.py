a = int(input('Введите значение выручки '))
b = int(input('Введите значение издержки '))

if a > b :
    print ('Ваша фирма в прибыли')
    c = a-b
    rent = (a/c)*100
    h = int(input('Введите количество сотрудников '))
    pay = c/h
    print ('Рентабельность состовляет ', rent)
    print ('Прибыль на одного сотрудника состовляет ', pay)

else:
    print ('Ваша фирма в убытке')