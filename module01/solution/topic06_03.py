# task 1
num = int(input('Число: '))

for i in range(1, num + 1):
    if i in range(5, 10):
        continue
    if i in range(17, 38):
        continue
    if i in range(78, 88):
        continue
    print(i)


# task 2
from random import randint
num = randint(0, 100)

while True:
    answer = input('Число: ')
    if answer == 'exit':
        break

    answer = int(answer)
    if answer == num:
        print('Угадано')
        break
    elif answer > num:
        print('Ваше число больше')
    elif answer < num:
        print('Ваше число меньше')
