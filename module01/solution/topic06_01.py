# task 1
for i in range(10):
    print("Я изучаю Python!")


# task 2
for i in range(6):
    print("AAA")
for i in range(6):
    print("BBBB")
print("E")
for i in range(9):
    print("TTTTT")
print("G")


# task 3
distance = int(input())
day = int(input())

for i in range(day):
    distance += distance * 0.1
print(distance)


# task 4
number = int(input())
bin = 128

for i in range(1, 9):
    if number >= bin:
        print("1", end="")
        number -= bin
    else:
        print("0", end="")
    bin //= 2
print()
