class Parent:

    def __init__(self, name, age, *childs):
        self.name = name
        self.age = age
        self.child_list = []
        self.child_add(*childs)

    def info(self):
        print('Имя: {}\nВозраст: {}\nСписок детей: {}\n'.format(
            self.name,
            self.age,
            ', '.join(self.child_list)
        ))

    def calm_down_child(self, child):
        if child.hunger == 3:
            print('Ребенок {}, нужно покормить!\n'.format(child.hungers[3]))
        else:
            child.state -= 1
            print('{}: {}\n'.format(
                child.name,
                child.states[child.state]
            ))

    def feed_child(self, child):
        child.hunger -= 1

    def child_add(self, *childs):
        for child in childs:
            if self.age - child.age > 16:
                self.child_list.append(child.name)
            else:
                print('Ну не мой это ребенок. Не видишь возраст? ')


class Child:
    states = {3: 'плачет', 2: 'ноет', 1: 'спокоен'}
    hungers = {3: 'очень голоден', 2: 'голоден', 1: 'сыт'}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.state = 3
        self.hunger = 3

    def info(self):
        print('Имя: {}\nВозраст: {}\nСостояние: {}\nГолод: {}\n'.format(
            self.name,
            self.age,
            self.states[self.state],
            self.hungers[self.hunger]
        ))


father = Parent('Pashik', 30)
son_1 = Child('Mark', 1)
son_2 = Child('Garri', 13)
father.child_add(son_1)
father.child_add(son_2)
father.info()
