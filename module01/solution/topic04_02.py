# task 1
weight = float(input('Вес десерта: '))

if 0 < weight < 2:
    print('Попробуйте корзиночки со сливками')
elif 2 <= weight <= 3:
    print('Как насчёт ассорти мини-тортиков?')
elif weight > 3:
    print('Рекомендуем многоярусный торт')
print('Переходите к покупкам!')


# task 2
height = int(input('Рост: '))
weight = int(input('Вес: '))
optimal_weight = height - 100

if weight > optimal_weight:
    print('Рекомендуем снизить вес')
elif weight < optimal_weight:
    print('Рекомендуем набрать вес')
else:
    print('Оптимальный вес')


# task 3
side_a = int(input('Сторона a:'))
side_b = int(input('Сторона b:'))
side_c = int(input('Сторона c:'))

if side_a == side_b == side_c:
    print('Равносторонний')
elif side_a == side_b or side_b == side_c or side_a == side_c:
    print('Равнобедренный')
else:
    print('Разносторонний')
