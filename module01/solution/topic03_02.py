# task 3
price    = int(input('Цена тура: '))
discount = int(input('Скидка в процентах: '))

price -= price * discount / 100
print(price)


# task 4
total_sum = int(input('Введите число '))
units     = total_sum % 10
dozens    = total_sum % 100 // 10
hundreds  = total_sum % 1000 // 100
thousands = total_sum // 1000

print('{} - 1р'.format(units))
print('{} - 10p'.format(dozens))
print('{} - 100р'.format(hundreds))
print('{} - 1000р'.format(thousands))


# task 5
a = int(input('Введите число a '))
b = int(input('Введите число b '))

print('Сумма квадратов:', a**2 + b**2)
print('Квадрат суммы:', (a + b)**2)
