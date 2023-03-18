from random import randint
# Список (list) - структура данных, для хранения объектов различных типов
# Список можно изменить

# Способы создания списка
# Квадратные скобки []
data1 = []
data2 = [78, True, 'Hello', 4.56]
print(data1)
print(data2)

# Функция list()
data1 = list()
data2 = list('Hello')
print(data1)
print(data2)

# Генерация списка
data1 = list(range(10))
data2 = [randint(-10, 10) for i in range(20)]
print(data1)
print(data2)


# Обращение к элементам списка
list1 = list(range(10, 100, 10))
print(list1[4])
print(list1[-1])
