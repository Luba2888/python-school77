from random import randint

# Task 1
students = ['Михайлова', 'Анисимов', 'Карпова', 'Елисеев', 'Тарасова']
print('Количество:', len(students))

students.sort()
num = 0
for student in students:
    num += 1
    print(num, student)


# Task 2
m = int(input())
numbers = list(range(1, m + 1))
print(numbers)


# Task 3
numbers = [randint(-20, 20) for i in range(10)]
print(numbers)
numbers = [num ** 2 for num in numbers]
print(numbers)
