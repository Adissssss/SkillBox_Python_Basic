print('Задача 6. Игра в кубики')

# Костя играет в азартную игру с кубиками с владельцем заведения.
# Правда, с довольно интересными правилами:
# если у Кости на кубике выпадет столько же или больше, чем у владельца,
# то Костя задолжает разность в тысячах долларов.
# Однако если выпадет меньше,
# то Косте выплатят столько тысяч долларов, сколько будет в сумме очков на кубиках.

# На вход в программу подаётся два числа.
# Если первое число больше либо равно второму,
# нужно вывести на экран их разность и отдельной строкой фразу: «Костя платит».
# В противном случае вывести их сумму и отдельной строкой — фразу: «Владелец платит».
# Также последней строкой в результате нужно вывести на экран фразу: «Игра окончена».

# Пример:
# Кубик Кости: 3
# Кубик владельца: 4
# Сумма: 7
# Владелец платит
# Игра окончена

num1 = int(input('number Kostya: '))
num2 = int(input('number Owner: '))
if num1 >= num2:
    print(num1 - num2)
    print('Kostya pays')
else:
    print(num1 + num2)
    print('Owner pays')

print('Game Over')