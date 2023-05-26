# Task 1
def calc_average(a, b):
    return (a + b) / 2


num1 = int(input("Введите число: "))
num2 = int(input("Введите число: "))
result = calc_average(num1, num2)
print(result)


# Task 2
def check_eligibility(score):
    return score >= 75


num_participants = int(input("Введите количество участников: "))
for i in range(num_participants):
    name = input("Введите имя участника: ")
    score = int(input("Введите балл участника: "))

    eligibility = check_eligibility(score)
    print(eligibility)


# Task 3
def check_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a


a = float(input("Введите длину 1-го отрезка: "))
b = float(input("Введите длину 2-го отрезка: "))
c = float(input("Введите длину 3-го отрезка: "))
d = float(input("Введите длину 4-го отрезка: "))

if check_triangle(a, b, c) or check_triangle(a, b, d) or check_triangle(a, c, d) or check_triangle(b, c, d):
    print("YES")
else:
    print("NO")


# Task 4
def calc_bmi(weight, height):
    return weight / ((height / 100) ** 2)


def bmi_category(bmi):
    if bmi < 17.5:
        return "Рекомендуется повышение веса."
    elif 17.5 <= bmi <= 23.0:
        return "Похудение не требуется."
    elif 23.1 <= bmi <= 35.0:
        return "Рекомендуется снижение массы тела."
    else:
        return "Необходимо немедленное снижение массы тела."


weight = float(input("Введите вес в килограммах: "))
height = float(input("Введите рост в сантиметрах: "))

bmi = calc_bmi(weight, height)
bmi_category = bmi_category(bmi)
print("Индекс массы тела (ИМТ):", bmi)
print("Рекомендации:", bmi_category)
