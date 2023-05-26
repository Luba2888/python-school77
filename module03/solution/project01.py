import time
import project01_auto

time.sleep(2)
print('Добро пожаловать в автоответчик!')
time.sleep(2)
print('Чтобы получить информацию о формате обучения, цене, времени обучения или поддержке, задайте вопрос.')
time.sleep(2)

while True:
    question = input('Введите вопрос: ')

    if 'формат обучения' in question:
        project01_auto.format_of()
    elif 'цена' in question:
        project01_auto.cena_start()
    elif 'информация' in question:
        project01_auto.more_info()
    elif 'время обучения' in question:
        project01_auto.time_info()
    elif 'поддержка' in question:
        project01_auto.support()
    elif 'выход' in question:
        print('Спасибо за использование автоответчика!')
        break
    else:
        print('Извините, не могу распознать ваш вопрос. Попробуйте еще раз.')
