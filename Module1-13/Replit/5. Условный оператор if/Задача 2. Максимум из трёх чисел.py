print('Задача 2. Максимум из трёх чисел')

# Как-то у нас уже было задание
# на нахождение максимума из трёх чисел с помощью дополнительной переменной.
# Теперь, когда вы знаете намного больше,
# вы можете оптимизировать программу, не тратя память компьютера на лишние переменные.

# Напишите программу,
# которая находит максимум из трёх чисел, не используя дополнительные переменны


a = int(input('enter 1 number : '))
b = int(input('enter 2 number: '))
c = int(input('enter 3 number: '))

if b < a > c:
    print('maximum value:', a)
elif a < b > c:
    print('maximum value:', b)
else:
    print('maximum value:', c)