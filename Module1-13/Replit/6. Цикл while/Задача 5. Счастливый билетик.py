print('Задача 5. Счастливый билетик')

# В старину, когда даже в столице билеты в общественном транспорте выдавали контролёры,
# существовало поверье:
# если на билете сумма первых трёх цифр в номере билета равна сумме последних трёх,
# то это к удаче.
#
# Напишите программу,
# которая получала бы на входе шестизначный номер билета
# и выводила, счастливый это билет или нет.
# К примеру, билеты 666 666 и 252 135 — счастливые,
# а 123 456 — нет.
# Подумайте, нужны ли для решения этой задачи циклы?

# Можно обойтись без циклов. Конструкция if/else справится с данной задачей.
# # var_1:
# num = int(input('enter the ticket number: '))
# first_sum = (num // (10 ** 5)) + (num // (10 ** 4) % 10) + (num // (10 ** 3) % 10)
# second_sum = (num % 10) + ((num % 100) // 10) + ((num % 1000) // 100)
# if first_sum == second_sum:
#   print('this is lucky ticket!!!')
# else:
#   print('this is not a lucky ticket')


# Циклы можно применить например вот так:

# var_2: бесконечный цикл

num = int(input('enter the ticket number: '))

first_sum = (num // (10 ** 5)) + (num // (10 ** 4) % 10) + (num // (10 ** 3) % 10)
second_sum = (num % 10) + ((num % 100) // 10) + ((num % 1000) // 100)
print(first_sum, second_sum)
while first_sum != second_sum:
  print('this is not a lucky ticket')
  num = int(input('enter the ticket number: '))
print('this is lucky ticket!!!')

# var_3:

# num = int(input('enter the ticket number: '))

# first_sum = (num // (10 ** 5)) + (num // (10 ** 4) % 10) + (num // (10 ** 3) % 10)
# second_sum = (num % 10) + ((num % 100) // 10) + ((num % 1000) // 100)
# while first_sum and second_sum != 0:
#   print(first_sum, second_sum)
#   if first_sum == second_sum:
#     print('this is lucky ticket!!!')
#     break
#   print('this is not a lucky ticket')
#   num = int(input('enter the ticket number: '))
