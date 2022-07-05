import math


def coin(x1, y1, r1):
    if math.sqrt(x1 ** 2 + y1 ** 2) <= r1:
        print('Монетка где-то рядом')
    else:
        print('Монетки в области нет')


print('Введите координаты монетки:')
x = float(input('X: '))
y = float(input('Y: '))
r = float(input('Введите радиус: '))

coin(x, y, r)
