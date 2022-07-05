from Deck import Deck
from Players import Player
from const import MESSAGES

uname = input('Введите свое имя: ')
player = Player(uname)
bot = Player()
deck = Deck()

for _ in range(2):
    player.take_card(deck.get_card())
    bot.take_card(deck.get_card())

player.print_cards()

while player.ask_card():
    player.take_card(deck.get_card())

    if player.full_points > 21:
        player.print_cards()
        print()
        bot.print_cards()
        print(MESSAGES.get('win').format(bot.name))
        break
    else:
        player.print_cards()
else:
    while bot.full_points < 16:
        bot.take_card(deck.get_card())
    player.print_cards()
    bot.print_cards()
    if player.full_points > bot.full_points:
        print(MESSAGES.get('win').format(player.name))
    elif bot.full_points == player.full_points:
        print(MESSAGES.get('drawn'))
    elif bot.full_points > player.full_points:
        print(MESSAGES.get('win').format(bot.name))
