N = int(input('Количество элементов списка: '))
K = int(input('Введите сдвиг: '))
number_list = []
new_number_list = []
for i in range(N):
    number = int(input('Введите число из списка: '))
    number_list.append(number)
print(f'Изначальный список: {number_list}')
if K <= len(number_list):
    for i in range(len(number_list)):
        new_number_list.append((number_list[number_list[i] - K - 1]))
    print(f"Новый список: {new_number_list}")
else:
    print(f'Введите сдвиг меньше {len(number_list)}')
