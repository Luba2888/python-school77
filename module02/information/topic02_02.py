# Длинна списка
data = list(range(10, 100, 10))
print(len(data))

# Срез списка
# [начало:конец]
data = list(range(10, 100, 10))
print(data[2:8])

# [начало:]
data = list(range(10, 100, 10))
print(data[5:])

# [:конец]
data = list(range(10, 100, 10))
print(data[:4])

# [:]
data = list(range(10, 100, 10))
print(data[:])

# [начало:конец:шаг]
data = list(range(10, 100, 10))
print(data[2:9:3])

# [::шаг]
data = list(range(10, 100, 10))
print(data[::-1])


# Операции над списками
# Объединение
print([2, 3, 5] + [0, 4, 6])

# Копирование
print([2, 3, 5] * 10)

# Минимальный элемент
print(min([2, 3, 5]))

# Максимальный элемент
print(max([2, 3, 5]))

# Сумма элементов
print(sum([2, 3, 5]))

# Перебор элементов
data = list(range(4, 10))
for i in data:
    print(i)

# Проверка элемента в списке
data = list(range(4, 10))
print(5 in data)

# Вывод в строку
data = list(range(10, 100, 10))
print(* data)
