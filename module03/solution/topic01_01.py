import math

# Task 1

def calc_circle_area(radius):
    return math.pi * radius ** 2


def calc_rectangle_area(length, width):
    return length * width


def calc_triangle_area(base, height):
    return 0.5 * base * height


shape = input("Введите форму (круг, прямоугольник, треугольник): ")
if shape == "круг":
    radius = float(input("Введите радиус круга: "))
    area = calc_circle_area(radius)
elif shape == "прямоугольник":
    length = float(input("Введите длину прямоугольника: "))
    width = float(input("Введите ширину прямоугольника: "))
    area = calc_rectangle_area(length, width)
elif shape == "треугольник":
    base = float(input("Введите основание треугольника: "))
    height = float(input("Введите высоту треугольника: "))
    area = calc_triangle_area(base, height)
else:
    print("Некорректный выбор формы.")
print(f"Площадь {shape}а равна {area}.")


# Task 2
def calc_segment_line(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


x1 = int(input("Введите значение x1: "))
y1 = int(input("Введите значение y1: "))
x2 = int(input("Введите значение x2: "))
y2 = int(input("Введите значение y2: "))
distance = calc_segment_line(x1, y1, x2, y2)
print(distance)
