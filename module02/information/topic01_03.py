# Методы строк
# Метод - функция, применяемая к объекту
# Вызов метода: имя_объекта.название_метода()

# count() - подсчет вхождений подстроки в строке
text = 'The Volga is the longest river in Europe'
print(text.count('i'))
print(text.count('i', 12))
print(text.count('i', 12, 30))

# find() - поиск индекса первого вхождения подстроки в строке
text = 'The Volga is the longest river in Europe'
print(text.find('Volga'))
print(text.find('i', 30))
print(text.find('i', 12, 30))

# rfind() - поиск индекса последнего вхождения подстроки в строке
text = 'The Volga is the longest river in Europe'
print(text.rfind('i'))

# lower() - создание копии строки в нижнем регистре
text = 'The Volga is the longest river in Europe'
print(text.lower())

# upper() - создание копии строки в верхнем регистре
text = 'The Volga is the longest river in Europe'
print(text.upper())

# split() - разбиение строки на подстроки в зависимости от разделителя
text = 'The Volga is the longest river in Europe'
print(text.split())
print(text.split('o'))

# join() - объединение строки в одну строку, вставляя между ними разделитель
text = 'The Volga is the longest river in Europe'.split()
print('|||'.join(text))

# ord() - получение кода символа
print(ord('a'))

# chr() - получение символа от номера кода
print(chr(35))
