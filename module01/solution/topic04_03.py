# task 1
weight  = int(input('Вес: '))
filling = input('Начинка: ')
price   = 0

if 0 <= weight <= 2500:
    price += 3000
elif weight > 2500:
    price += 5000

if filling == 'фрукты':
    price += 1000
elif filling != '':
    price += 500    
print(price)


# task 2
num1      = int(input('Число: '))
num2      = int(input('Число: '))
operation = input('Операция: ')

if operation == '+':
    print(num1 + num2)
elif operation == '-':
    print(num1 - num2)
elif operation == '*':
    print(num1 * num2)
elif operation == '/':
    if num2 == 0:
        print('На ноль делить нельзя!')
    else:
        print(num1 / num2)
else:
    print('Неверная операция')
