guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
while True:
    print(f'Сейчас на вечеринке {len(guests)} человек: {guests}')
    guest = input('Гость пришел или ушел?: ')
    if guest == 'пришел':
        name = input('Имя гостя: ')
        if len(guests) > 6:
            print(f'Прости, {name}, но мест нет.')
        elif len(guests) < 6:
            guests.append(name)
            print(f'Привет, {name}')
    elif guest == 'ушел':
        name = input('Имя гостя: ')
        print(f'Пока, {name}!')
        guests.remove(name)
    elif guest == 'пора спать':
        print('Вечеринка закончилась, все легли спать.')
        break
