# Task 1
print('*')
print('**')
print('***')
print('****')
print('*****')
print('******')
print('*******')


# Task 2
num1 = int(input('Число 1: '))
num2 = int(input('Число 2: '))
num3 = int(input('Число 3: '))

sum = num1 + num2 + num3
print('Sum:', sum)


# Task 3
x = int(input('x: '))
y = int(input('y: '))

print('{} + {} = ?'.format(x, y))
print('{} | {} | {}'.format(x, y, x + y))
print('Z({})=F({})'.format(x, y))
print('x={}; y={};'.format(x, y))
print('Ответ: ({};{})'.format(x, y))


# Task 4
name         = input('Имя: ')
age          = int(input('Возраст: '))
century      = 100
current_year = 2022

hundredth_year = century - age + current_year
print('{}, 100 лет Вам исполнится в {} году'.format(name, hundredth_year))


# Task 5
digit        = input('Цифра от 1 до 9: ')
single_digit = int(digit)
dual_digit   = int(digit * 2)
triple_digit = int(digit * 3)

sum = single_digit + dual_digit + triple_digit
print(sum)


# Task 6
client_name = input('Имя: ')
tour_count  = int(input('Количество купленных ранее туров: '))
tour_name   = input('Предлагаемый тур: ')

message = '''{0}: {1}: {2} 
Здравствуйте Вы путешествовали с нами уже {1} раз(а)! 
Хотите снова? Наша турфирма проводит распродажу. 
Тур в {2} со скидкой 50%!'''.format(client_name, tour_count, tour_name)

print(message)
