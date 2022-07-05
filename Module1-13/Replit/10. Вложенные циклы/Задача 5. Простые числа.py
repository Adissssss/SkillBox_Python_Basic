print('Задача 5. Простые числа')

# Напишите программу,
# которая считает количество простых чисел в заданной последовательности
# и выводит ответ на экран.

n = int(input('Введите конечное число последовательности: '))
count = 0
for i in range(2, n + 1):
    for j in range(2, i):
        if i % j == 0:
            # print(i, j, end = ' ')
            break
    else:
        # print(i, end = ' ')
        count += 1
    print()
print(count)
