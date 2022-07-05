import random


def f(x, y):
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    return x / y


def f2(x, y):
    x -= random.randint(0, 10)
    y -= random.randint(0, 5)
    return y / x


with open('coordinates.txt', 'r') as file:
    for line in file:
        nums_list = line.split()
        try:
            res1 = f(int(nums_list[0]), int(nums_list[1]))
        except ZeroDivisionError:
            res1 = 0
        try:
            res2 = f2(int(nums_list[0]), int(nums_list[1]))
        except ZeroDivisionError:
            res2 = 0
        number = random.randint(0, 100)
        with open('result.txt', 'a') as file_2:
            my_list = sorted([str(res1), str(res2), str(number)])
            file_2.write(' '.join(my_list))
            file_2.write('\n')
