def selection_number(my_number_list):
    for i_min in range(len(my_number_list)):
        for index in range(i_min, len(my_number_list)):
            if my_number_list[index] < my_number_list[i_min]:
                my_number_list[index], my_number_list[i_min] = my_number_list[i_min], my_number_list[index]
    return my_number_list


N = int(input('Количество элементов списка: '))
number_list = []
for i in range(N):
    number = int(input('Введите число из списка: '))
    number_list.append(number)
print(f'Изначальный список: {number_list}')
print(f'Отсортированный список: {selection_number(number_list)}')
