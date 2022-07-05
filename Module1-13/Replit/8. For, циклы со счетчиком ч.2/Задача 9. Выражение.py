print('Задача 9. Выражение')

# Дано число x.
# Напишите программу для вычисления следующего выражения

# ((x-1)(x-3)(x-7)…(x-63)/
# ((x-2)(x-4)(x-8)…(x-64))


# x = int(input('введите Х: '))
# a  = 1
# b = 1
# try:
#   for n in range(1, 7):
#     a *= x - (2 ** n - 1)
#     b *= x - 2 ** n
#   print(a / b)
# except ZeroDivisionError:
#   print('на ноль делить нельзя!')


x = int(input('введите Х: '))
for i in 2, 4, 8, 16, 32, 64:
    if x == i:
        print('В знаменателе получится 0. На ноль делить нельзя!')
        break
    else:
        a = 1
        b = 1
        for n in range(1, 7):
            a *= x - (2 ** n - 1)
            b *= x - 2 ** n
print(a / b)

