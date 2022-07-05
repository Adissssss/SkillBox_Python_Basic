import random


class Potato:
    states = {0: 'Отсутствует', 1: 'Росток', 2: 'Зеленая', 3: 'Зрелая'}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def is_ripe(self):
        if self.state == 3:
            return True
        return False

    def print_state(self):
        print('Картошка {} сейчас {}'.format(
            self.index,
            Potato.states[self.state]
        ))

    def collect(self):
        self.state = 0
        print('Картошка {} выкопана'.format(self.index))


class PotatoGarden:

    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range(1, count + 1)]

    def grow_all(self):
        print('Картошка прорастает!')
        for i_potato in self.potatoes:
            i_potato.grow()

    def are_all_ripe(self):
        if not all([i_potato.is_ripe() for i_potato in self.potatoes]):
            print('Картошка не созрела!\n')
        else:
            print('Вся картошка созрела. Можно собирать!\n')

    def collect_potato(self):
        for potato in self.potatoes:
            potato.collect()
        self.potatoes.clear()


class Gardener:
    care_list = ['полита', 'прополота']

    def __init__(self, name='Grower'):
        self.name = name
        self.gardens = []

    def plant_garden(self, num_garden, num_potato):
        for garden in range(1, num_garden + 1):
            self.gardens.append(PotatoGarden(num_potato))
        print('Садовник {}\nПосадил грядок: {}\nРастений на грядке: {}\n'.format(
            self.name,
            len(self.gardens),
            num_potato
        ))

    def take_care(self):
        care = random.choice(self.care_list)
        for i, garden in enumerate(self.gardens):
            print('Грядка {} {}'.format(i + 1, care))
            garden.grow_all()
            print()

    def check_garden(self):
        for i, garden in enumerate(self.gardens):
            print('{} грядка'.format(i + 1))
            garden.are_all_ripe()

    def harvest(self):
        for i, garden in enumerate(self.gardens):
            print('{} грядка'.format(i + 1))
            garden.collect_potato()
            print('Грядка {} пустая {}'.format(i + 1, garden.potatoes))


sadovnik = Gardener()
sadovnik.plant_garden(2, 5)
sadovnik.take_care()
sadovnik.take_care()
sadovnik.take_care()
sadovnik.check_garden()
sadovnik.harvest()
