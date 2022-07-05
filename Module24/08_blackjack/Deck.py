from itertools import product
from random import shuffle
from const import *


class Card:

    def __init__(self, suit, rank, points):
        self.suit = suit
        self.rank = rank
        self.points = points

    def __str__(self):
        card = '[{} {}]-{}'.format(
            self.rank,
            self.suit,
            self.points
        )
        return card


class Deck:

    def __init__(self):
        self.cards = self.generate_deck()
        shuffle(self.cards)

    def generate_deck(self):
        cards = []
        for suit, rank in product(suits, ranks):
            c = Card(suit=suit, rank=rank, points=ranks[rank])
            cards.append(c)
        return cards

    def get_card(self):
        return self.cards.pop()

    def __len__(self):
        return len(self.cards)
