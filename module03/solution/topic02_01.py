import random
import time
import calendar

# Task 1
def check_ticket(number):
    if number == 2020:
        return "Вы выиграли 1000 рублей!"
    return "Повезет в следующий раз!"


ticket_number = random.randint(1000, 9999)
result = check_ticket(ticket_number)
print(result)


# Task 2
start = time.time()
input()
end = time.time()
print(end - start)


# Task 3
print(calendar.month(2023, 2))


# Task 4
free_days = []
for i in range(1, 13):
    c = calendar.monthcalendar(2023, i)
    first_week = c[0]
    third_week = c[2]
    fourth_week = c[3]

    if first_week[calendar.THURSDAY]:
        free_day = third_week[calendar.THURSDAY]
    else:
        free_day = fourth_week[calendar.THURSDAY]

    s = f'{free_day} {calendar.month_name[i]}'
    free_days.append(s)
print(", ".join(free_days))
