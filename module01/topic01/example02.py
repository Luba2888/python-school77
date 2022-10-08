# Форматирование строки
# format() - форматирует указанное(ые) значение(я) и вставляет их внутрь заполнителя строки
# Заполнитель задается с помощью фигурных скобок: {}
print("My name is {1}, I'm {0}".format(30,"Marina"))
print("My name is {}, I'm {}".format("Ivan",25))

# Типы форматирования
# Выравнивание влево
print("I have {:<10} rubles.".format(50))
# Выравнивание вправо
print("I have {:>10} rubles.".format(50))
# Выравнивание по центру
print("I have {:^10} rubles.".format(50))
# Знак числа в крайнее левое положение 
print("I have {:=10} rubles.".format(-50))

# Двоичная система счисления
print("I have {:b} rubles.".format(50))
# Десятичная система счисления
print("I have {:d} rubles.".format(50))
# Восьмеричная система счисления
print("I have {:o} rubles.".format(50))
# Шестнадцатеричная система счисления
print("I have {:x} rubles.".format(50))
print("I have {:X} rubles.".format(50))

# Экспоненциальная запись
print("I have {:e} rubles.".format(50))
print("I have {:E} rubles.".format(50))
# Процент
print("I have {:%} rubles.".format(50))