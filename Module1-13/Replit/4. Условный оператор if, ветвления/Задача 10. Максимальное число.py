print('Задача 10. Максимальное число (по желанию)')

# Пользователь вводит три числа.
# Напишите программу,
# которая выводит на экран максимальное из этих трёх чисел (все числа разные).
# Можно использовать дополнительные переменные, если нужно

a = int(input('a= '))
b = int(input('b= '))
c = int(input('c= '))

if b < a > c:
  print(a)
if a < b > c:
  print(b)
if a < c > b:
  print(c)