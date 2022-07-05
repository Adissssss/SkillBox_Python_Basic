def winner_list(new_dict):
    winners = {}
    place = 0
    for key, value in sorted(new_dict.items(), reverse=True):
        if len(value) == 1 and value[0] not in winners and place != 3:
            winners[value[0]] = key
            place += 1
        else:
            for name in value:
                if name not in winners and place != 3:
                    winners[name] = key
                    place += 1
    for i, res in enumerate(winners.items()):
        print('{place} место. {name} ({point})'.format(
            place=i + 1,
            name=res[0],
            point=res[1]
        ))


protocol_dict = {}
N = int(input('Сколько записей вносится в протокол?\n'))
print('Записи (результат и имя):')
for i in range(1, N + 1):
    result = input(f'{i} запись: ').split()
    if int(result[0]) in protocol_dict.keys():
        protocol_dict[int(result[0])] += (result[1],)
    else:
        protocol_dict[int(result[0])] = (result[1],)
print('Итоги соревнований:')
winner_list(protocol_dict)
