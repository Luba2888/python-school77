from random import randint
type = ('Камень', 'Бумага', 'Ножницы')

while True:
    player_score = 0
    comp_score = 0
    round = 1
    while player_score < 3 and comp_score < 3:
        player = int(input('Введите номер: 1.Камень 2.Бумага 3.Ножницы: '))
        comp = randint(1, 3)
        if player not in (1, 2, 3):
            continue

        print('Компьютер выбрал', type[comp - 1])
        game = (player - comp) % 3
        if game == 0:
            print('Ничья')
        elif game == 1:
            print('Вы выиграли')
            player_score += 1
        elif game == 2:
            print('Вы проиграли')
            comp_score += 1
        round += 1
        print()

    if player_score == 3:
        print('Победа')
    else:
        print('Проигрыш')

    answer = input('Сыграем еще? Да/Нет')
    if answer != 'Да':
        break
