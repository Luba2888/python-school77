# Task 1
s = input()
n = len(s)
part_1 = (s[:(n + (n % 2)) // 2])
part_2 = (s[(n + (n % 2)) // 2:])
print(part_2 + part_1)


# Task 2
s = input()
print(s[1:5])
print(s.upper())
print(s.replace('*', '@'))
print(input().replace('1', 'one'))


# Task 3
first_name = input()
patronymic = input()
last_name = input()
position = input()
print(first_name[0] + '.', patronymic[0] + '.', last_name + ',', position)


# Task 4
text = input().lower()
letter = input()
print(text.find(letter), text.rfind(letter))


# Task 5
text = input().lower()
start = input()
end = input()
print(text.startswith(start))
print(text.endswith(end))


# Task 6
length1 = len(input('Напишите подробный отзыв:'))
length2 = len(input('Что вам понравилось:'))
length3 = len(input('Что вам НЕ понравилось:'))
length = (length1 + length2 + length3) * 10 / 100
print('Спасибо! Ваша скидка:', length)
