# Task 1
char = input()

if 'a' <= char <= 'z':
    print('Строчная латинская буква')
else:
    print('Не строчная латинская буква')


# Task 2
feedback = input('Отзыв: ')
feedback = feedback.lower()

pos_fun = feedback.find('весело')
pos_fascinating = feedback.find('увлекательно')
pos_entertainment = feedback.find('развлечения')

if pos_fun == -1:
    pos_fun = 'Не найдено'
if pos_fascinating == -1:
    pos_fascinating = 'Не найдено'
if pos_entertainment == -1:
    pos_entertainment = 'Не найдено'

print('Весело:', pos_fun, '\nУвлекательно:',
      pos_fascinating, '\nРазвлечения:', pos_entertainment)


# Task 3
feedback = input('Блюда: ')
feedback = feedback.lower()
print(feedback.find('шашлык'), feedback.find('шоколадный торт'))


# Task 4
text = input()
open = text.find('(')
close = text.rfind(')')
print(text[:open] + text[close + 1:])
