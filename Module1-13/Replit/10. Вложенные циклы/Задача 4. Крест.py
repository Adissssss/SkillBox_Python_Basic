print('Задача 4. Крест')

# Напишите программу,
# которая выводит на экран крест из символов “^”.
#
# (Символы выводятся по диагоналям воображаемого квадрата.)


# ^        ^
#  ^      ^
#   ^    ^
#    ^  ^
#     ^^
#     ^^
#    ^  ^
#   ^    ^
#  ^      ^
# ^        ^



size = int(input('Введите размер креста: '))
for row in range(1, size):
  for col in range(1, size):
    if col + row == size:
      print('^', end = '')
    elif row - col == 0:
      print('^', end = '')
    else:
      print(' ', end = '')
  print()
