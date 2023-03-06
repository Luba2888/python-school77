# Task 1
vowels = 'аяуюоеёэиыAЯУЮОЕЁЭИЫaeiouyAEIOUY'
text = input()
count = 0

for char in text:
    if char in vowels:
        count += 1
print(count)


# Task 2
text = input()
result = ''

space_count = 0
for char in text:
    if char == ' ':
        space_count += 1
    else:
        space_count = 0
    if space_count < 2:
        result += char
print(result)


# Task 3
text = input()
result = ''

for char in text:
    if char == 'а':
        result += 'б'
    elif char == 'б':
        result += 'а'
    elif char == 'А':
        result += 'Б'
    elif char == 'Б':
        result += 'А'
    else:
        result += char
print(result)


# Task 4
text = input()
right = len(text) - 1
left = 0

flag = True
while right < left:
    if text[right] != text[left]:
        flag = False
        break
    right -= 1
    left += 1

if flag:
    print('Палиндром')
else:
    print('Не палиндром')
