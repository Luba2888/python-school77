import random
import time

hello_list = ['привет', 'добрый', 'хай', 'здравствуй', 'здорова']
exit_list = ['всего доброго', 'выход', 'пока', 'до свидания', 'прощай', 'бб']
game_titles = '0 1 2 3 4 5 6 7 8 9 A B C D E F'
game_pos = '0123456789ABCDEF'

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

    elif message in ['игра', 'играть']:

        print("ʘ‿ʘ: Игра 'Поиск алмазов'")
        print('''
               .    '    ,
                 _______
            _  .`_|___|_`.  _
                \ \   / /
                 \ ' ' /
                  \ ' /   
                   \./
                    V
        ''')
        print('В одной из коробок лежит алмаз @')
        print('С ботом по очереди открывайте коробки')
        print('Кто первый найдет, тот победил')
        print('Кто найдет крест X, тот проигрывает досрочно')
        message = input('Нажмите Enter для старта игры').lower()
        print('\n\nСтарт игры')

        diamond = random.randint(0, 15)
        while True:
            cross = random.randint(0, 15)
            if cross != diamond:
                break
        line = ['█'] * 16
        comp_memory = list(range(0, 16))
        game = 0

        # Старт игры
        while True:
            # Вывод
            print(game_titles)
            print(' '.join(line))
            print('\n')

            if game != 0:
                print(message)
                break

            # Игрок
            print('Под каким символом открыть коробку?')
            choice = input('Вы: ')

            player = game_pos.find(choice)
            if player not in comp_memory:
                print('Коробка уже открыта! Пропуск хода')
            elif player == diamond:
                line[player] = '@'
                message = 'Вы выиграли!'
                game = 1
            elif player == cross:
                line[player] = 'X'
                message = 'Вы проиграли!'
                game = -1
            else:
                line[player] = '░'
            comp_memory.remove(player)

            # Вывод
            print(game_titles)
            print(' '.join(line))
            print('\n')

            if game != 0:
                print(message)
                break

            # Компьютер
            print('Под каким символом открыть коробку?')
            time.sleep(0.8)
            computer = random.choice(comp_memory)
            print('ʘ‿ʘ:', game_pos[computer])

            if computer == diamond:
                line[computer] = '@'
                message = 'Вы проиграли!'
                game = -1
            elif computer == cross:
                line[computer] = 'X'
                message = 'Вы выиграли!'
                game = 1
            else:
                line[computer] = '░'
            comp_memory.remove(computer)

    else:
        print('ʘ_ʘ: Я не знаю такой темы')
    print()
print('ʘ‿ʘ: Всего доброго!')
