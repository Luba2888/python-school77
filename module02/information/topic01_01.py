# Строка (str) - тип данных, состоящая из последовательности символов
# Строки нельзя изменить


# Способы создания строки
# Одинарные или двойные кавычки
name = 'Ivan Ivanov'
year = '30'
print(name, year)

# Тройные кавычки
text = '''1. First
2. Second
3. Third'''
print(text)

# Функция str()
num = str(123)
print(num)


# Операции над строками
# Сложение (конкатенация)
a = 'Sa'
b = 'ma'
c = 'ra'
print(a + b + c)

# Умножение
name = 'Ivan'
print(name * 10)

# Оператор принадлежности: in
string = 'Samara'
sub_1 = 'ma'
sub_2 = 'mr'

print(sub_1 in string)
print(sub_2 in string)

# Сравнение: >, <, >=, <=, ==, !=
fruit_1 = 'banana'
fruit_2 = 'apple'
print(fruit_1 > fruit_2)


# Характеристики строк
# Длинна строки
text = 'Hello, world!'
print(len(text))

# Индексация
text = 'Hello, world!'
print(text[0])
print(text[4])
print(text[-1])
