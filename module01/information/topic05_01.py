# Типы данных

# int - тип данных, сокращение от слова integer (целое)
number = 5
print(type(number))

# float - тип данных, число с плавающей запятой
number = 7.32
print(type(number))

# string - тип данных, строка
text = "Строка"
print(type(text))

# bool - тип данных, логический
exp = True
print(type(True))


# int() - преобразование в целое число
number1 = int("75")
number2 = int(45.5)
number3 = int(True)
print(number1, number2, number3)

# float() - преобразование в вещественное число
number1 = float(84)
number2 = float("75")
number3 = float(True)
print(number1, number2, number3)

# str() - преобразование в строку
text1 = str(84)
text2 = str(45.5)
text3 = str(True)
print(text1, text2, text3)

# bool() - преобразование в логический тип
exp1 = bool(84)
exp2 = bool("75")
exp3 = bool(45.5)
print(exp1, exp2, exp3)


# min() - определение минимального числа
min_number = min(-12, 4, 5, -7)
print(min_number)

# max() - определение максимального числа
max_number = max(-12, 4, 5, -7)
print(max_number)

# abs() - вычисление модуля числа
number = abs(-10)
print(number)

# round() - округление числа
number = round(59.555555, 2)
print(number)


# Модуль math, импортируются все функции модуля
import math

# Импортирование определенных функций модуля math
from math import sqrt, sin

# Число пи
print(math.pi)

# Число эйлера
print(math.e)

# Положительная бесконечность
print(math.inf)

# math.log() - логарифм
print(math.log(1024, 2))

# math.pow() - возведение в степень
print(math.pow(2, 10))

# math.sqrt() - квадратный корень
print(math.sqrt(25))

# math.sin() - синус
print(math.sin(60))

# math.cos() - косинус
print(math.cos(60))

# math.tan() - тангенс
print(math.tan(60))
