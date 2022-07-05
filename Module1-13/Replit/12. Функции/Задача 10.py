print('Задача 10')

# Напишите игру - текстовый квест.
# Игрок находится в квартире, его задача - покинуть ее.
#
# Игрок свободно перемещается по квартире, пока не покинет ее.
#
# В квартире есть три комнаты (спальня, кухня, ванна) и коридор.
# В ванну можно попасть из коридора и спальни.
# В спальню можно попасть из ванны и коридора.
# На кухню можно попасть только из коридора.
# Коридор связан со всеми комнатами, но в нем дополнительно есть дверь наружу.
# На кухне открыто окно.
# Если игрок пытается выбраться через него, то разбивается и проигрывает


# Пример:

# Вы в спальне. Куда идем?
# 1 - в ванну
# 2 - в коридор

# 2

# Вы в коридоре. Куда идем?
# 1 - в спальню
# 2 - в ванну
# 3 - на кухню
# 4 - в дверь

# 2

# Вы в ванне. Куда идем?
# 1 - в коридор
# 2 - в спальню

# 2

# Вы в спальне...
import random


def quest_menu():
    print('Добро пожаловать в Эскейп-рум\nЧтобы начать игру нажмите введите "play"\nДля выхода из игры введите "exit"')
    act = input('..')
    if act == 'play':
        quest_game()
    elif act == 'exit':
        print()


def quest_game():
    room = ['коридор', 'спальня', 'кухня', 'ванна']
    start_place = random.choice(room)
    print(f'Игра началась, вы в комнате {start_place}')
    if start_place == 'коридор':
        corridor()
    elif start_place == 'спальня':
        bedroom()
    elif start_place == 'кухня':
        kitchen()
    else:
        bath()


def corridor():
    print('Вы в корридоре. Куда идем?\n1 - в спальню\n2 - в ванну\n3 - на кухню\n4 - закрытая дверь')
    while True:
        move = int(input('..'))
        if move == 1:
            bedroom()
            break
        elif move == 2:
            bath()
            break
        elif move == 3:
            kitchen()
            break
        elif move == 4:
            closedDoor()
            break
        else:
            print('Выбери доступное направление!')


def bath():
    print('Вы в ванной. Куда идем?\n1 - в спальню\n2 - в коридор\n3 - посмотреть на запотевшее зеркало')
    while True:
        move = int(input('..'))
        if move == 1:
            bedroom()
            break
        elif move == 2:
            corridor()
            break
        elif move == 3:
            mistmirror()
            break
        else:
            print('Выбери доступное направление!')


def kitchen():
    print(
        'Вы на кухне. Куда идем?\n1 - в коридор\n2 - посмотреть в открытое окно\n3 - на подоконнике что-то нацарапано')
    while True:
        move = int(input('..'))
        if move == 1:
            corridor()
            break
        elif move == 2:
            openWindow()
            break
        elif move == 3:
            windowsill()
            break
        else:
            print('Выбери доступное направление!')


def bedroom():
    print('Вы в спальне. Куда идем?\n1 - в коридор\n2 - в ванну')
    while True:
        move = int(input('..'))
        if move == 1:
            corridor()
            break
        elif move == 2:
            bath()
            break
        else:
            print('Выбери доступное направление!')


def closedDoor():
    print('На двери кодовый замок')
    print('* - для отмены')
    while True:
        code = input('password: ')
        if code == '1408':
            print('Дверь открыта! Квест пройден!')
            print('\nGame Over')
            break
        elif code == '*':
            corridor()
            break
        else:
            print('Не верный пароль')


def mistmirror():
    print('На запотевшем зеркале что-то написано...\n1 - посмотреть на зеркало.')
    move = int(input('..'))
    if move == 1:
        print('anti_log(3.1486)')
        bath()
    else:
        bath()


def windowsill():
    print('На подоконнике что-то нацарапано...\n1 - Посмотреть поближе')
    move = int(input('..'))
    if move == 1:
        print('аккуратней, не упади.')
        kitchen()
    else:
        kitchen()


def openWindow():
    print('Ты упал и разбился... \nКонец игры!')
    print('\n')
    # print('Чтобы начать заново введите "play"\nДля выхода в главное меню - "menu"')
    return print()
    # act = input('..')
    # if act == 'play':
    #   quest_game()
    # elif act == 'menu':
    #   quest_menu()


quest_menu()