# task 1
question = input('Вопрос: ')

while question != 'off':
    if question != '':
        print('Обращение отправлено: ')
    question = input('Вопрос: ')
print("До свидания!")


# task 2
num = int(input("Число: "))
div = 2

print('Простые множители:', end=' ')
while num != div:
    if num % div == 0:
        num /= div
        print(div, end=' ')
    else:
        div += 1
print(div)


# task 3
deposit = int(input('Вклад: '))
rate    = int(input('Процент: '))
target  = int(input('Цель: '))
year    = 0

while deposit < target:
    deposit *= 1 + rate / 100
    deposit = int(100 * deposit) / 100
    year += 1
print(year)
