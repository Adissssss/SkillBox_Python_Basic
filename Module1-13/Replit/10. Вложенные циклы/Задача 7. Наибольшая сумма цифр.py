print('Задача 7. Наибольшая сумма цифр')

# Вводится N чисел.
# Среди натуральных чисел, которые были введены,
# найдите наибольшее по сумме цифр. Выведите на экран это число и сумму его цифр.
res_summ = 0
N = int(input('Сколько чисел нужно посчитать? ..'))
for i in range(1, N + 1):
  num = current_num = int(input('Введите число: '))
  current_summ = 0
  while num != 0:
    digit = num % 10
    current_summ += digit
    num //= 10
  if current_summ > res_summ:
    res_summ = current_summ
    number = current_num
  # print(f'Сумма цифр: {res_summ}')
  print()
else:
  print(f'наибольшая сумма цифр: {res_summ}, число {number}')




