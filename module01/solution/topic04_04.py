# task 1
answer = input('Хотите узнать хиты продаж? ')

if answer == 'да':
    category = input('Категория товаров? ')
    if category == 'продукты':
        print('Молоко 1л, Печенье с изюмом, Персики')
    else:
        print('Стиральный порошок, Щётка для обуви')
else:
    print('Дайте знать, если передумаете!')


# task 2
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


# task 3
num = int(input('Число: '))

if num % 2 == 0:
    if num >= 2 and num <= 5:
        print('NO')
    elif num >= 6 and num <= 20:
        print('YES')
    elif num > 20:
        print('NO')
else:
    print('YES')
