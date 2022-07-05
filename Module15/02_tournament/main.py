name_list = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
first_day_list = []
for i in range(0, len(name_list), 2):
    first_day_list.append(name_list[i])
print(f'Первый день: {first_day_list}')
