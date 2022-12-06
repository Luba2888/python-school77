# Task 1
students1 = int(input('Учеников в классе #1: '))
students2 = int(input('Учеников в классе #2: '))
students3 = int(input('Учеников в классе #3: '))
capacity  = 2

desks1 = students1 // capacity + students1 % capacity
desks2 = students2 // capacity + students2 % capacity
desks3 = students3 // capacity + students3 % capacity
total_desks = desks1 + desks2 + desks3
print(total_desks)


# Task 2
rate    = int(input('Ставка: '))
rubles  = int(input('Вклад в рублях: '))
kopecks = int(input('Вклад в копейках: '))

kopecks_before = 100 * rubles + kopecks
kopecks_after  = int(kopecks_before * (100 + rate) / 100)

print('Вклад через год:', end=' ')
print(kopecks_after // 100, kopecks_after % 100)
