phonebook_dict = {
    'Сидоров Алексей': 3452,
    'Сидорова Алена': 3243,
    'Сидоров Ян': 1257,
    'Иванов Петр': 9876,
    'Иванова Галя': 4567,
    'Иванова Света': 1234
}

while True:
    action = (input('Действие: "добавить контакт" или "найти человека по фамилии" в списке контактов?\n'))
    if action == 'добавить контакт':
        new_name = input('Введите имя и фамилию контакта: ')
        phone_number = input('Введите номер телефона: ')
        count = 0
        for name in phonebook_dict:
            if new_name.lower() == name.lower():
                count += 1
        if count < 1:
            phonebook_dict[new_name] = phone_number
            print('Словарь контактов: ', phonebook_dict)
        else:
            print('Этот человек уже есть в словаре.')
    elif action == 'найти человека по фамилии':
        find_dict, count = {}, 0
        sername = input('Введите фамилию человека?\n')
        for i_name, i_number in phonebook_dict.items():
            res = i_name.split()
            if sername.lower() == res[0].lower():
                find_dict[i_name] = i_number
                count += 1
        if count > 1:
            print('Список контактов: ', find_dict)
        else:
            print('Такого контакта в списке нет.')
