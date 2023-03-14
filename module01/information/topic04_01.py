# Ветвления

# Вывод "Совпадение" если две строки равны
first_text = input()
second_text = input()
if first_text == second_text:
    print("совпадение")
print(first_text, second_text)


# Проверка делимости числа на пять
number = int(input())
if number % 5 == 0:
    print("Число кратно пяти")
else:
    print("Число не кратно пяти")


# Сравнение двух чисел
a = int(input())
b = int(input())
if a > b:
    print("Число 'a' больше")
elif a < b:
    print("Число 'b' больше")
else:
    print("Числа равны")
