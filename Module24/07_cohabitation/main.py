from random import randint


class People:

    def __init__(self, name):
        self.satiety = 50
        self.name = name
        self.home = None

    def info(self):
        print('Имя: {}\nадрес проживания: {}\nДенег в копилке: {}\nСытость: {}'.format(
            self.name,
            self.home.adress,
            self.home.money,
            self.satiety
        ))

    def check_into(self, home):
        if isinstance(home, Home):
            self.home = home

    def eat(self):
        self.satiety += 1
        self.home.take_food()
        return '{} ест: сытость {}, еда {}'.format(
            self.name,
            self.satiety,
            self.home.food
        )

    def work(self):
        self.satiety -= 1
        self.home.give_money()
        return '{} работает: сытость {}, деньги {}'.format(
            self.name,
            self.satiety,
            self.home.money
        )

    def play(self):
        self.satiety -= 1
        return '{} играет: сытость {}'.format(
            self.name,
            self.satiety
        )

    def shopping(self):
        self.home.take_money()
        self.home.give_food()
        return '{} идет в магазин: еда {}, деньги {}'.format(
            self.name,
            self.home.food,
            self.home.money
        )

    def action_one_day(self):
        number_cubes = randint(1, 6)
        if self.satiety < 20 and self.home.food >= 10:
            text = self.eat()
        elif self.home.food < 10:
            text = self.shopping()
        elif self.home.money < 50:
            text = self.work()
        elif number_cubes == 1:
            text = self.work()
        elif number_cubes == 2:
            text = self.eat()
        else:
            text = self.play()
        print(text)
        return 0

    def alive(self):
        if self.satiety > 0:
            return True
        else:
            return False


class Home:
    food = 50
    money = 0

    def __init__(self, adress='Unknown'):
        self.adress = adress

    def info(self):
        print('Адрес: {}\nЕды в холодильнике: {}\nДенег в копилке: {}'.format(
            self.adress,
            self.food,
            self.money
        ))

    def take_money(self):
        self.money -= 1

    def give_money(self):
        self.money += 1

    def take_food(self):
        self.food -= 1

    def give_food(self):
        self.food += 1


people_1 = People('Вася')
people_2 = People('Марина')
home = Home('Каховского, 40')
people_1.home = home
people_2.home = home

for i in range(1, 366):
    print(f'День {i}')
    people_1.action_one_day()
    people_2.action_one_day()
    if not people_1.alive():
        print('{} умер. Сытость: {}. Эксперимент завершен неудачно.'.format(
            people_1.name,
            people_1.satiety
        ))
        break
    elif not people_2.alive():
        print('{} умер. Сытость: {}. Конец симуляции.'.format(
            people_2.name,
            people_2.satiety
        ))
        break
    if i == 365:
        print('Эксперимент завершен успешно!')
