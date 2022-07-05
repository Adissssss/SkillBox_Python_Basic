number = int(input('Количество человек: '))
K = int(input('Какое число в считалке? '))
print(f'Значит, выбывает каждый {K} человек')
people_list = list(range(1, number + 1))
out = 0
for i in range(number - 1):
    print(f'Текущий круг людей: {people_list}')
    start_count = out % len(people_list)
    out = (start_count + K - 1) % len(people_list)
    print(f'Начало счёта с номера {people_list[start_count]}')
    print(f'Выбывает человек под номером {people_list[out]}')
    people_list.remove(people_list[out])
print(f'Остался человек под номером {people_list[0]}')
