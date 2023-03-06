from random import randint

# Task 1
numbers = [randint(-20, 20) for i in range(10)]
print(numbers)

min_index = numbers.index(min(numbers))
max_index = numbers.index(max(numbers))
print(min_index, max_index)


# Task 2
numbers = [randint(-20, 20) for i in range(10)]
print(numbers)

min_index = 0
max_index = 0
for i in range(len(numbers)):
    if numbers[i] < numbers[min_index]:
        min_index = i
    if numbers[i] > numbers[max_index]:
        max_index = i

print(min_index, max_index)


# Task 3
numbers = [randint(-20, 20) for i in range(10)]
print(numbers)

min_index = numbers.index(min(numbers))
max_index = numbers.index(max(numbers))
left = min(min_index, max_index)
right = max(min_index, max_index)

print(sum(numbers[left + 1: right]))
