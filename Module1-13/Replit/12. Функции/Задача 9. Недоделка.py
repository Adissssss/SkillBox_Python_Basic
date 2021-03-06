print('Задача 9. Недоделка')

# Вы пришли на работу в контору по разработке игр,
# целевая аудитория которых - дети и их родители.
#
# У прошлого программиста было задание
# сделать две игры в одном приложении, чтобы пользователь мог выбирать одну из них.
#
# Однако программист, на место которого вы пришл
# и, перед увольнением не успел сделать эту задачу и оставил только небольшой шаблон проекта.
#
# Используя этот шаблон,
# реализуйте игры «Камень, ножницы, бумага» и «Угадай число».
#
# Правила игры «Камень, ножницы, бумага»:
# программа запрашивает у пользователя строку
# и выводит победил он или проиграл.
#
# Камень бьёт ножницы, ножницы режут бумагу, бумага кроет камень.
#
# Правила игры “Угадай число”:
# программа запрашивает у пользователя число до тех пор, пока он его не отгадает.
import random


def rock_paper_scissors():
    print('камень ножницы бумага\nДля выхода в меню напиши "выход"')
    print()
    user_choise = ''
    while user_choise != 'выход':
        user_choise = input('Сделай выбор — камень, ножницы или бумага: ')
        comp_choise = random.randint(1, 4)
        if comp_choise == user_choise:
            print(f'Оба пользователя выбрали {user_choise}. Ничья!')
        elif user_choise == "камень":
            if comp_choise == 2:
                print('Камень бьет ножницы! Вы победили!')
            else:
                print('Бумага оборачивает камень! Вы проиграли.')
        elif user_choise == "бумага":
            if comp_choise == 1:
                print("Бумага оборачивает камень! Вы победили!")
            else:
                print("Ножницы режут бумагу! Вы проиграли.")
        elif user_choise == "ножницы":
            if comp_choise == 3:
                print("Ножницы режут бумагу! Вы победили!")
            else:
                print("Камень бьет ножницы! Вы проиграли.")


def guess_the_number():
    num = random.randint(1, 100)
    print('Угадай число. От 1 до 100.')
    ans = 0
    while ans != num:
        ans = int(input('..'))
        if ans > num:
            print('Попробуй меньше :)')
        elif ans < num:
            print('Попробуй больше :)')
        else:
            print('Угадал!')
    print()


def mainMenu():
    choise = 0
    while choise != 3:
        print('Выбери игру:\n1 - "Камень, ножницы, бумага"\n2 - "Угадай число"\n3 - Выход из приложения')
        choise = int(input('..'))
        if choise == 1:
            rock_paper_scissors()
        elif choise == 2:
            guess_the_number()
        elif choise == 3:
            break


mainMenu()