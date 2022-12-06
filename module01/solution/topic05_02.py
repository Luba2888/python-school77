# task 1
from math import sqrt, pi
figure = input("Прямоугольник, Треугольник или Круг? ")

if figure == "Прямоугольник":
    side_a = int(input())
    side_b = int(input())
    area = side_a * side_b
    print("%4.2f" % area)

elif figure == "Треугольник":
    side_a = int(input())
    side_b = int(input())
    side_c = int(input())
    p = (side_a + side_b + side_c) / 2
    area = sqrt(p * (p - side_a) * (p - side_b) * (p - side_c))
    print("%4.2f" % area)

elif figure == "Круг":
    radius = int(input())
    area = pi * radius**2
    print("%4.2f" % area)


# task 2
from math import tan, pi
n = int(input(''))
a = float(input(''))

area = (n * a**2) / (4 * tan(pi / n))
print("%4.2f" % area)
