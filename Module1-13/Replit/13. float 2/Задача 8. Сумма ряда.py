print('Задача 8. Сумма ряда')

# Пользователь вводит действительное число
# "х" и точность "precision".

# P.S: Формулу смотреть на сайте :)


# Напишите программу,
# которая по число х вычисляет сумму ряда в точности до precision.


# Операцией возведения в степень и функцией factorial пользоваться нельзя.

# Пример:
# Введите точность: 0.001

# Введите x: 5
# Сумма ряда =  0.2836250150891709


def factorial(n):
  factorial = 1
  for i in range(1, n + 1):
    factorial *= i
  return factorial


def degree(x, n):
  Xdegree = 1
  for i in range(1, n + 1):
    Xdegree *= x
  return Xdegree

precision = float(input('Точность: '))
x = int(input('Введите x: '))
addMember = 1
result = 0
n = 0


while abs(addMember) > precision:
  addMember = degree(-1, n) * (degree(x, (2 * n)) / factorial(2 * n))
  result += addMember
  n += 1
print(f'Сумма ряда: {result}') 