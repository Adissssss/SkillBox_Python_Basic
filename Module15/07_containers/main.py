container_list = []
number_containers = int(input('Количество контейнеров: '))
for i in range(number_containers):
    while True:
        weigth = int(input('Введите вес контейнера:'))
        if 1 < weigth < 200:
            container_list.append(weigth)
            break
        else:
            print('Некоректная масса контейнера. Вес контейнера не должен превышать 200')
print(container_list)
new_weigth = int(input('Введите вес нового контейнера: '))
for i in range(len(container_list)):
    if new_weigth > container_list[i]:
        print(f'Номер, куда встанет новый контейнер: {i + 1}')
        break
    elif new_weigth < container_list[-1] or new_weigth == container_list[-1]:
        print(f'Номер, куда встанет новый контейнер: {len(container_list) + 1}')
        break
