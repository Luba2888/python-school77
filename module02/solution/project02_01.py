hello_list = ['привет', 'добрый', 'хай', 'здравствуй', 'здорова']
exit_list = ['всего доброго', 'выход', 'пока', 'до свидания', 'прощай', 'бб']

# Приветствие
print('Поздоровайтесь с чат-ботом, чтобы начать')
while True:
    message = input('Вы: ').lower()
    has_hello = False

    for hello in hello_list:
        if hello in message:
            has_hello = True
            break

    if has_hello:
        break
    print('ʘ‿ʘ: Я Вас не понимаю')

# Общение
print('ʘ‿ʘ: Здравствуйте!')
while True:
    print('ʘ‿ʘ: О чем хотите поговорить?')
    message = input().lower()

    if message in exit_list:
        break

    if message in ['погода', 'о погоде']:
        print('ʘ‿ʘ: Какая сегодня погода у вас?')
        message = input().lower()

        if message in ['солнце', 'облачно', 'ясно', 'хорошая']:
            print('ʘ‿ʘ: Замечательно!')
        elif message in ['дождь', 'снег', 'слякоть', 'плохая', 'сильный ветер']:
            print('ʘ︿ʘ: Сочувствую')
        else:
            print('ʘ_ʘ: Я такое не знаю')

    elif message in ['eда', 'о еде', 'питание']:
        print('ʘ‿ʘ: Какую еду предпочитаете?')
        message = input().lower()

        if message in ['фрукты', 'овощи', 'ягоды', 'зелень']:
            print('ʘ‿ʘ: Здорово! Это полезно')
        elif message in ['газировки', 'конфеты', 'фастфуд']:
            print('ʘ︿ʘ: Рекомендую не злоупотреблять')
        else:
            print('ʘ_ʘ: Я такое не знаю')
    else:
        print('ʘ_ʘ: Я не знаю такой темы')

print('ʘ‿ʘ: Всего доброго!')
