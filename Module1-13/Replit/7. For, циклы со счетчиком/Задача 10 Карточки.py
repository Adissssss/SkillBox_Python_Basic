print('Задача 10 Карточки.')

#Для настольной игры используются карточки с номерами от 1 до N.
# Одна карточка потерялась.
# Найдите ее, зная номера оставшихся карточек.
#
# Вводится число N,
# далее еще N − 1 чисел: я
# номера оставшихся карточек (различные числа от 1 до N).
# Программа должна вывести номер потерянной карточки.


summ = 0
N = int(input('enter number of card: '))
for i in range(1, N + 1):
  summ += i
for i in range(1, N):
  card_num = int(input('enter remaining card numbers: '))
  summ -= card_num
  # print(summ)
print(f'lost card is number {summ}')

