import topic02_02_rules
import topic02_02_password

# Task 1
print('Сегодня в программе:\n1-футбол\n2-хоккей\n3-теннис')
answer = input('Ваш выбор:')

if answer == "1":
    topic02_02_rules.print_football()
elif answer == "2":
    topic02_02_rules.print_hockey()
elif answer == "3":
    topic02_02_rules.print_tennis()


# Task 2
password = input("Введите пароль: ")

if topic02_02_password.check(password):
    print("Ваш пароль является надежным.")
else:
    print("Ваш пароль не соответствует требованиям надежности.")
