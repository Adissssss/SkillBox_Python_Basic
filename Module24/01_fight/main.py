import random


class Warrior:

    def __init__(self, name='Unknown', health=100, damage=20):
        self.health = health
        self.damage = damage
        self.name = name

    def info(self):
        print('name = {}\nhp = {}\ndmg = {}'.format(
            self.name,
            self.health,
            self.damage
        ))

    def dead(self):
        if self.health <= 0:
            return '{} убит'.format(self.name)

    def hit_enemy(self, enemy):
        enemy.health -= 20
        print('{} атаковал {}.\nУ {} осталось {} hp\n'.format(
            self.name,
            enemy.name,
            enemy.name,
            enemy.health
        ))
        enemy.dead()


parya = Warrior('parya')
barya = Warrior('barya')

while True:
    x = random.randint(0, 1)
    if x == 0:
        parya.hit_enemy(barya)
        if barya.dead():
            print(barya.dead())
            break
    else:
        barya.hit_enemy(parya)
        if parya.dead():
            print(parya.dead())
            break
