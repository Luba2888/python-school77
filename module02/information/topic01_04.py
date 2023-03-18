# Форматирование строк с помощью format()
# Одна подстановка
text = '{0}, Apple, Peach'.format('Banana')
print(text)

# Несколько подстановок
text = '{0}, {1}, {0}, Peach'.format('Banana', 'Apple')
print(text)

# Множественные подстановки с именем
text = '{a}, {b}, Peach'.format(b='Banana', a='Apple')
print(text)


# Сравнение строк
print('a' < 'b')
print('A' < 'a')
print('app' < 'apple')
print('0' < 'a')
print('apple' == 'apple')
