# task 1
fahrenheit = float(input('Температура в градусах Фаренгейта: '))
celsius = 5 / 9 * (fahrenheit - 32)
print(celsius)


# task 2
num1    = int(input('Число 1: '))
num2    = int(input('Число 2: '))
num3    = int(input('Число 3: '))
num4    = int(input('Число 4: '))
num5    = int(input('Число 5: '))
min_num = min(num1, num2, num3, num4, num5)
max_num = max(num1, num2, num3, num4, num5)

print(min_num, max_num)


# task 3
from math import sqrt
side = input('Какую сторону (a, b, c) вы хотите рассчитать? ')

if side == 'a':
    b = int(input('Введите длину стороны b: '))
    c = int(input('Введите длину стороны c: '))
    print(sqrt(c**2 - b**2))
elif side == 'b':
    a = int(input('Введите длину стороны a: '))
    c = int(input('Введите длину стороны c: '))
    print(sqrt(c**2 - a**2))
elif side == 'a':
    a = int(input('Введите длину стороны a: '))
    b = int(input('Введите длину стороны b: '))
    print(sqrt(a**2 + b**2))
else:
    print('Неверное название стороны')


# task 4
from math import sqrt
a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))

d = b**2 - 4 * a * c
if d > 0:
    x1 = (-b + sqrt(d)) / (2 * a)
    x2 = (-b - sqrt(d)) / (2 * a)
    print(x1, x2)
elif d == 0:
    x = -b / (2 * a)
    print(x)
else:
    print('Корней нет')
