print('Задача 8. НОД')

# #Напишите функцию, вычисляющую наибольший общий делитель двух чисел


def NOD():
  a = int(input('Введите первое число: '))
  b = int(input('Введите второе число: '))
  while a != 0 and b != 0:
    if a > b:
      a %= b
    else:
      b %= a
  print(a + b)

NOD()




# max = (a + b + abs(a - b)) / 2
# min = (a + b - abs(a - b)) / 2
# if max % min == 0:
#   print(f'Наибольший общий делитель: {min}')