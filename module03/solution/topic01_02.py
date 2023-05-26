# Task 1
def calc_median(a, b, c):
    return a + b + c - min(a, b, c) - max(a, b, c)


a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))
median = calc_median(a, b, c)
print(median)


# Task 2
def calc_bonus_salary(name, last_name, salary=120000, bonus=10):
    bonus_amount = int(salary + (bonus / 100))
    total_salary = salary + bonus_amount

    print(f"Новогодняя премия для сотрудника {name} {last_name}: {bonus_amount}")
    print(f"Зарплата с учетом премии: {total_salary}")


calc_bonus_salary("Иван", "Иванов")
calc_bonus_salary("Елена", "Смирнова", 200000, 20)
calc_bonus_salary("Петр", "Петров", salary=150000)
calc_bonus_salary("Анна", "Сидорова", bonus=15)
