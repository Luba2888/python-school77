# Task 1
tel = input('Введите телефон по шаблону: x (xxx) xxxxxx: ')
print(tel[0] + tel[3:6] + tel[8:])


# Task 2
text = input()
result = ''
while text[0] == ' ':
    text = text[1:]

while text[-1] == ' ':
    text = text[:-1]


space_count = 0
for char in text:
    if char == ' ':
        char = '-'
        space_count += 1
    else:
        space_count = 0
    if space_count < 2:
        result += char

print(result)


# Task 3
text = input()

if text == text[::-1]:
    print('Палиндром')
else:
    print('Не палиндром')
