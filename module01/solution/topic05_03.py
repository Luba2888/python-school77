# task 1
from random import randrange
num1 = randrange(6, 12, 2)
num2 = randrange(5, 101, 5)
print(num1, num2)


# task 2
from math import tan, pi
n = int(input())
s = float(input())

area = (n * s**2) / (4 * tan(pi / n))
print("%4.2f" % area)


# task 3
from math import pi
radius = float(input())
area   = pi * radius ** 2
volume = 4 / 3 * pi * radius**3
print(area, volume)


# task 4
from random import randrange
number = randrange(38)

if number == 37:
    print("Выпавший номер: 00")
    print("Выигравшая ставка: 00")
else:
    print("Выпавший номер:", number)
    print("Выигравшая ставка:", number)

if number in (1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36):
    print("Выигравшая ставка: Красное")
elif number != 0 and number != 37:
    print("Выигравшая ставка: Черное")

if 0 < number < 37:
    if number % 2 == 0:
        print("Выигравшая ставка: Четное")
    else:
        print("Выигравшая ставка: Нечетное")

if 1 <= number <= 18:
    print("Выигравшая ставка: от 1 до 18")
elif 19 <= number <= 36:
    print("Выигравшая ставка: от 19 до 36")
