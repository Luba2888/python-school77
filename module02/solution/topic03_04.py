from random import randint

# Task 1
numbers = [randint(-20, 20) for i in range(10)]
print(numbers)

target_num = int(input('Введите число из списка: '))
numbers.remove(target_num)
print(numbers)


# Task 2
numbers = []

while True:
    num = int(input('Введите число: '))
    if num == 0:
        break
    numbers.append(num)

numbers.sort()
for num in numbers:
    print(num)
