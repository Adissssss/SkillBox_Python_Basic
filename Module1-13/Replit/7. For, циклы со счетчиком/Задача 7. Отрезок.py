print('Задача 7. Отрезок')

# Напишите программу,
# которая считывает с клавиатуры два числа a и b,
# считает и выводит на консоль
#среднее арифметическое всех чисел из отрезка [a; b], которые кратны числу 3.

a = int(input('a = '))
b = int(input('b = '))
count, summ = 0, 0
for i in range(a, b + 1):
  if i % 3 == 0:
    summ += i
    count += 1
print(f'arithmetic mean value = {summ / count}')