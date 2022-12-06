# task 1
num = int(input('Число: '))

if 100 <= num <= 999:
    print('Трёхзначное')
else:
    print('Не трёхзначное')


# task 2
x = int(input('x: '))
y = int(input('y: '))

if x > 0 and y > 0:
    print('I четверть')
elif x < 0 and y > 0:
    print('II четверть')
elif x < 0 and y < 0:
    print('III четверть')
elif x > 0 and y < 0:
    print('IV четверть')
else:
    print('На оси')


# task 3
a = int(input('Сторона a: '))
b = int(input('Сторона b: '))
c = int(input('Сторона c: '))

if a + b > c and a + c > b and b + c > a:
    print('Невырожденный треугольник существует')
else:
    print('Невырожденный треугольник не существует')


# task 4
spending = int(input('Сумма: '))

if  0 < spending < 500:
    print('Попробуйте пирожные со сгущенкой!')
elif 500 <= spending <= 1000:
    print('Побалуйте себя тортиком Секрет!')
elif spending > 1000:
    print('Угоститесь шоколадным фонданом с голубикой!')


# task 5
year = int(input('Введите год: '))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('Високосный')
else:
    print('Невисокосный')


# task 6
wish = input('Ваши пожелание: ')

if wish == 'крем':
    print('Попробуйте заварные пирожные')
elif wish == 'изюм':
    print('Попробуйте фирменные кексы')
else:
    print('Попробуйте рогалики с маком')
