number = int(input('Введите число:'))
number_list = []
for i in range(1, number):
    if i % 2 != 0:
        number_list.append(i)
print(f'Список нечетных чисел от 1 до N: {number_list}')
