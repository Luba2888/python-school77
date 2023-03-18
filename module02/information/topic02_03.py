# Методы списков
# Добавление в конец
data = [10, 20, 30, 40, 50]
data.append(33)
print(data)

# Очистка
data = [10, 20, 30, 40, 50]
data.clear()
print(data)

# Копия
data = [10, 20, 30, 40, 50]
list_copy = data.copy()
print(list_copy)

# Подсчет элементов
data = [10, 20, 30, 40, 50]
print(data.count(20))

# Добавление элементов другого списка
data = [10, 20, 30, 40, 50]
data2 = [15, 25, 35, 45, 55]
data.extend(data2)
print(data)

# Поиск индекса указанного элемента
data = [10, 20, 30, 40, 50]
print(data.index(40))

# Вставка в список
data = [10, 20, 30, 40, 50]
data.insert(2, 155)
print(data)

# Удаление из списка
data = [10, 20, 30, 40, 50]
data.pop(2)
print(data)

# Переворот
data = [10, 20, 30, 40, 50]
data.reverse()
print(data)

# Сортировка
data = [50, 14, 63, 35, 7]
data.sort()
print(data)
