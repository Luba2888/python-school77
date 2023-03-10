from random import randint, choice

# Task 1
numbers = [randint(-20, 20) for i in range(10)]
print(numbers)
print(len(numbers))
print(numbers[-1])
print(numbers[::-1])

if 5 in numbers and 17 in numbers:
    print('YES')
else:
    print('NO')

print(numbers[1:-1])

# Task 2
text = input().lower()
text = ' ' + text + ' '
print(text.count(' a ') + text.count(' an ') + text.count(' the '))

# Task 3
negative   = []
positive = []
zero = []
while True:
    num = input()
    if num == '':
        res = negative + zero + positive
        break

    num = int(num)
    if num < 0:
        negative.append(num)
    elif num == 0:
        zero.append(num)
    else:
        positive.append(num)

for num in res:
    print(num)

# Task 4
ticket = []
dropped = []
numbers = list(range(1, 50))

while len(ticket) < 6:
    num = randint(1, 49)
    if num not in ticket:
        ticket.append(num)

for i in range(6):
    dropped.append(choice(numbers))
    numbers.remove(dropped[-1])

dropped.sort()
ticket.sort()
print(dropped)
print(ticket)

if dropped == ticket:
    print('win')
else:
    print('lose')
