# while - цикл с предусловием

# while работает при выполнении условия
i = 0
while (i < 10):
    print(i)
    i += 1

# else после while выполняется после завершения цикла
# else не является обязательным
i = 0
sum = 0
while (i < 10):
    sum += i
    i += 1
else:
    print("Сумма:", sum)

# Условие в цикле может содержать логические операции, как в условии в блоке if
a = 5
b = 0
while a < 10 or b < 10:
    print(a, b)
    a += 1
    b += 1
