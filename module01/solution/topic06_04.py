# task 1
from math import sqrt

first_x = float(input('x: '))
first_y = float(input('y: '))
prev_x = first_x
prev_y = first_y
str = input('x: ')
perimeter = 0

while str != '':
    x = float(str)
    y = float(input('y: '))
    dist = sqrt((prev_x - x)**2 + (prev_y - y)**2)
    prev_x = x
    prev_y = y
    perimeter += dist
    str = input('x: ')

dist = sqrt((x - first_x)**2 + (y - first_y)**2)
perimeter += dist
print(perimeter)


# task 2
BABY_PRICE   = 0.00
CHILD_PRICE  = 14.00
ADULT_PRICE  = 23.00
SENIOR_PRICE = 18.00

BABY_AGE_LIMIT  = 2
CHILD_AGE_LIMIT = 12
ADULT_AGE_LIMIT = 64

total_price = 0
while True:
    str = input('Возраст: ')
    if str == '':
        break

    age = int(str)
    if age <= BABY_AGE_LIMIT:
        total_price += BABY_PRICE
    elif age <= CHILD_AGE_LIMIT:
        total_price += CHILD_PRICE
    elif age <= ADULT_AGE_LIMIT:
        total_price += ADULT_PRICE
    else:
        total_price += SENIOR_PRICE

print(total_price)
