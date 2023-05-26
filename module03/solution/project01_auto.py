import time


def format_of():
    print('Какой формат обучения Вы рассматриваете? 1 - онлайн, 2 - офлайн')
    y = input('Введите команду: ')
    if y == '1':
        cxz = 'online'
        print('Загрузка...')
        time.sleep(5)
        print('Вы выбрали', cxz, '- обучение')
        cena_start()
    elif y == '2':
        cxz = 'offline'
        print('Загрузка...')
        time.sleep(5)
        print('Вы выбрали', cxz, '- обучение')
        cena_pro()
    else:
        print('Неверная команда. Попробуйте еще раз.')
        format_of()


def cena_start():
    print('Цена на онлайн-обучение: 100$')
    more_info()


def cena_pro():
    print('Цена на офлайн-обучение: 200$')
    more_info()


def more_info():
    print('Хотите узнать больше информации? 1 - да, 2 - нет')
    choice = input('Введите команду: ')
    if choice == '1':
        print('Дополнительная информация: Пока отсутствует')
    elif choice == '2':
        print('Спасибо за обращение!')
    else:
        print('Неверная команда. Попробуйте еще раз.')
        more_info()


def time_info():
    print('Каково время проведения обучения?')
    print('Длительность обучения: 1 год')


def support():
    print('Если у вас есть вопросы или нужна помощь, обратитесь в службу поддержки.')
    print('Контактная информация: +79991111111')
