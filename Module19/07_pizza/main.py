order_list = []
N = int(input('Введите кол-во заказов: '))
for i in range(1, N + 1):
    order = input(f'{i} заказ: ').split()
    order[2] = int(order[2])
    order_list.append(order)
order_dict = {}
for element in order_list:
    name = element[0]
    pizza = element[1]
    count = element[2]
    if name not in order_dict:
        order_dict[name] = {pizza: count}
    else:
        if pizza not in order_dict[name]:
            order_dict[name].update({pizza: count})
        else:
            order_dict[name][pizza] += count
for name in sorted(order_dict):
    print(f'{name}:')
    for pizza, count in sorted(order_dict[name].items()):
        print(f'{pizza}: {count}')
