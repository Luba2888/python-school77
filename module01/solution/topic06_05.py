# # task 1
num1 = int(input('Число 1: '))
num2 = int(input('Число 2: '))

sum1 = 0
for i in range(1, num1):
    if num1 % i == 0:
        sum1 += i

sum2 = 0
for i in range(1, num2):
    if num2 % i == 0:
        sum2 += i

if sum1 == num2 and sum2 == num1:
    print('Дружественные')
else:
    print('Недружественные')


# task 2
num = input('Число: ')

while num != 'off':
    if num != '1':
        mood = input('Настроение: ')
    if mood == 'веселое':
        print('Мультфильм Шрек')
    else:
        print('Мультфильм Алладин')


# task 3
max_num = 0
count = 0
num = -1

while num != 0:
    num = int(input('Число: '))
    if num > max_num:
        max_num = num
        count = 1
    elif num == max_num:
        count += 1

print(count)
