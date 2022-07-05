import abc
from const import MESSAGES


class AbstractPlayer(abc.ABC):

    def __init__(self, name='Bot'):
        self.name = name
        self.cards = []
        self.full_points = 0

    @abc.abstractmethod
    def ask_card(self):
        pass

    def change_points(self):
        self.full_points = sum([card.points for card in self.cards])

    def take_card(self, card):
        self.cards.append(card)
        if card.rank == 'туз':
            if self.full_points + card.points > 21:
                card.points = 1
                self.change_points()
            else:
                card.points = 11
                self.change_points()
        self.change_points()

    def print_cards(self):
        print('{}:'.format(self.name))
        for card in self.cards:
            print(card)
        print('очков: {}\n'.format(self.full_points))


class Player(AbstractPlayer):

    def ask_card(self):
        choice = input(MESSAGES.get('ask_card'))
        print()
        if choice == 'y':
            return True
        else:
            return False
