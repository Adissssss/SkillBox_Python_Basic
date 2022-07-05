WIN_COMB = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]


class Pole:
    pole = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    def __init__(self):
        self.__init_board()

    def __init_board(self):
        print('-' * 13)
        for i in range(3):
            print('|', self.pole[0 + i * 3], '|', self.pole[1 + i * 3], '|', self.pole[2 + i * 3], '|')
            print('-' * 13)

    def draw_sing(self, sing):
        while True:
            index = (input('\nКуда поставить {}:  '.format(sing)))
            if index not in self.pole:
                print('Выберите свободную клетку на поле!')
            else:
                self.pole[int(index) - 1] = sing
                self.__init_board()
                break

    def __check_winner(self, comb):
        for (x, y, z) in comb:
            if self.pole[x - 1] == self.pole[y - 1] and self.pole[y - 1] == self.pole[z - 1]:
                return True
        else:
            return False

    def select_sing(self):
        choice = input('Кто ходит первый? Х/О \n').lower()
        while choice != 'x' and choice != 'o':
            print('Введите Х или О!')
            choice = input('Кто ходит первый? Х/О \n').lower()
        return True if choice == 'x' else False

    def play_game(self):
        if self.select_sing():
            while True:
                self.draw_sing('X')
                if self.__check_winner(WIN_COMB):
                    print('X выиграл')
                    break
                self.draw_sing('O')
                if self.__check_winner(WIN_COMB):
                    print('O выиграл')
                    break
        else:
            while True:
                self.draw_sing('O')
                if self.__check_winner(WIN_COMB):
                    print('O выиграл')
                    break
                self.draw_sing('X')
                if self.__check_winner(WIN_COMB):
                    print('X выиграл')
                    break


pole = Pole()
pole.play_game()
