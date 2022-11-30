# Вложенные циклы
# Работает с циклами for и while
for i in range(10):
    for j in range(10):
        for k in range(10):
            print(i, j, k)


# Алгоритм Евклида - нахождение наибольшего общего делителя(НОД) двух чисел

# 1 Вариант
a = 120
b = 345
while a != 0 and b != 0:
    if a > b:
        a %= b
    else:
        b %= a
print(a + b)

# 2 Вариант
a = 120
b = 345
while a != b:
    if a > b:
        a -= b
    else:
        b -= a
print(a)
