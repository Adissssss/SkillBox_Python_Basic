number_skate = int(input('Количество коньков: '))
size_skate_list = []
for i in range(1, number_skate + 1):
    size_skate = input(f'Размер {i} пары: ')
    size_skate_list.append(size_skate)
number_people = int(input('Количество людей: '))
size_people_list = []
for i in range(1, number_people + 1):
    size_people = input(f'Размер ноги {i} человека: ')
    size_people_list.append(size_people)
situation_list = []
count = 0
for i in size_people_list:
    for j in range(len(size_skate_list)):
        if size_skate_list[j] >= i:
            size_skate_list.remove(size_skate_list[j])
            count += 1
            break
print(f'Наибольшее кол-во людей, которые могут взять ролики: {count}')
