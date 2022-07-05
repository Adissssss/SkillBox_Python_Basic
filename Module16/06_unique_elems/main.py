list_1, list_2 = [], []
for i in range(3):
    number_1 = int(input('Введите числа первого списка: '))
    list_1.append(number_1)
for i in range(7):
    number_2 = int(input('Введите числа второго списка: '))
    list_2.append(number_2)
print(f'Первый список: {list_1}')
print(f'Второй список: {list_2}')
list_1.extend(list_2)
for i in list_1:
    for j in range(list_1.count(i) - 1):
        list_1.remove(i)
print(f'Новый список с уникальными элементами: {list_1}')
