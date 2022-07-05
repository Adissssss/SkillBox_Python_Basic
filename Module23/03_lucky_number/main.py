import random

errors = [ValueError, BaseException, ArithmeticError]
sym = 0
try:
    while sym <= 777:
        num = int(input('Введите число: '))
        with open('licky_number.txt', 'a') as file:
            file.write(str(num) + '\n')
        sym += num
        if random.random() < 0.08:
            err = random.choice(errors)
            raise err
except (ValueError, BaseException, ArithmeticError):
    print('Вас постигла неудача')
else:
    print('Условие для выхода выполнено.')
