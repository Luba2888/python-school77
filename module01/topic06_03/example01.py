# Операторы в цикле

# break - осуществляет выход из цикла
# Работает в for и while
for i in range(10):
    if i == 5:
        break
    print(i)

# continue - осуществляет переход на следующий шаг до завершения итерации цикла
for i in range(10):
    if i == 5 or i == 7:
        continue
    print(i)
