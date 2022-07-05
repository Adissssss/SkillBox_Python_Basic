print('Задача 7. Ход конём')

# В рамках разработки шахматного ИИ стоит новая задача.
# По заданным вещественным координатам коня
# и второй точки программа должна определить может ли конь ходить в эту точку.
#
# Используйте как можно меньше конструкций if и логических операторов.
# Обеспечьте контроль ввода.

# Введите местоположение коня:
# 0.071
# 0.118
# Введите местоположение точки на доске:
# 0.213
# 0.068
# Конь в клетке (0, 1). Точка в клетке (2, 0).
# Да, конь может ходить в эту точку.
while True:
  print('Введите местоположение фигуры:')
  xH = float(input('X - '))
  yH = float(input('y - '))
  xHorse = int(xH * 10)
  yHorse = int(yH * 10)
  print('Введите местоположение точки:')
  xP = float(input('X - '))
  yP = float(input('y - '))
  xPoint = int(xP * 10)
  yPoint = int(yP * 10)
  if xHorse < 0 or xHorse > 7 or yHorse < 0 or yHorse > 7:
    print('Введите корректные данные!')
    print()
  elif xPoint < 0 or xPoint > 7 or yPoint < 0 or yPoint > 7:
    print('Введите корректные данные!')
    print()
  else:
    break
print(f'Координаты фигуры: {xHorse}, {yHorse}')
print(f'Координаты точки: {xPoint}, {yPoint}')
if (xPoint == xHorse - 2 or xPoint == xHorse + 2) and (yPoint == yHorse - 1 or yPoint == yHorse + 1):
  print('Конь может ходить в эту точку!')
elif (xPoint == xHorse - 1 or xPoint == xHorse + 1) and (yPoint == yHorse - 2 or yPoint == yHorse + 2):
  print('Конь может ходить в эту точку!')
else:
  print('Конь не может ходить в эту точку.')


















print('Задача 7. Ход конём')

# В рамках разработки шахматного ИИ стоит новая задача.
# По заданным вещественным координатам коня
# и второй точки программа должна определить может ли конь ходить в эту точку.
#
# Используйте как можно меньше конструкций if и логических операторов.
# Обеспечьте контроль ввода.

# Введите местоположение коня:
# 0.071
# 0.118
# Введите местоположение точки на доске:
# 0.213
# 0.068
# Конь в клетке (0, 1). Точка в клетке (2, 0).
# Да, конь может ходить в эту точку.
while True:
  print('Введите местоположение фигуры:')
  xH = float(input('X - '))
  yH = float(input('y - '))
  xHorse = int(xH * 10)
  yHorse = int(yH * 10)
  print('Введите местоположение точки:')
  xP = float(input('X - '))
  yP = float(input('y - '))
  xPoint = int(xP * 10)
  yPoint = int(yP * 10)
  if xHorse < 0 or xHorse > 7 or yHorse < 0 or yHorse > 7:
    print('Введите корректные данные!')
    print()
  elif xPoint < 0 or xPoint > 7 or yPoint < 0 or yPoint > 7:
    print('Введите корректные данные!')
    print()
  else:
    break
print(f'Координаты фигуры: {xHorse}, {yHorse}')
print(f'Координаты точки: {xPoint}, {yPoint}')
if (xPoint == xHorse - 2 or xPoint == xHorse + 2) and (yPoint == yHorse - 1 or yPoint == yHorse + 1):
  print('Конь может ходить в эту точку!')
elif (xPoint == xHorse - 1 or xPoint == xHorse + 1) and (yPoint == yHorse - 2 or yPoint == yHorse + 2):
  print('Конь может ходить в эту точку!')
else:
  print('Конь не может ходить в эту точку.')






































