# Экранированные последовательности
# Нестандартные символы в строке

# Новая строка
text = 'Hello\nworld'
print(text)

# Обратный слэш
text = 'Hello\\world'
print(text)

# Апостроф
text = 'Hello\'world'
print(text)

# Кавычка
text = 'Hello\'world'
print(text)

# BackSpace
text = 'Hello\bworld'
print(text)

# Перевод формата
text = 'Hello\fworld'
print(text)

# Возврат каретки
text = 'Hello\rworld'
print(text)

# Горизонтальная табуляция
text = 'Hello\tworld'
print(text)

# Вертикальная табуляция
text = 'Hello\vworld'
print(text)

# Символ Unicode 16-бит
text = 'Hello\u2211world'
print(text)

# Символ Unicode 32-бит
text = 'Hello\U0001F642world'
print(text)


# Срез строки
# Извлечение подстроки из строки

# [начало:конец]
text = 'Ivan Ivanov'
print(text[2:8])

# [начало:]
text = 'Ivan Ivanov'
print(text[5:])

# [:конец]
text = 'Ivan Ivanov'
print(text[:4])

# [:]
text = 'Ivan Ivanov'
print(text[:])

# [начало:конец:шаг]
text = 'Ivan Ivanov'
print(text[2:9:3])

# [::шаг]
text = 'Ivan Ivanov'
print(text[::-1])
