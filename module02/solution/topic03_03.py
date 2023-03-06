from random import randint

# Task 1
numbers = [randint(-20, 20) for i in range(10)]
print(numbers)

numbers[1] = 0
numbers += [1, 2, 3]
numbers *= 2
print(numbers)


# Task 2
words = []

while True:
    word = input('Введите слово: ')
    if word == '':
        break

    if word not in words:
        words.append(word)
print(words)
