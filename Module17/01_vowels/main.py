text = input('Введите текст: ')
letters = [i for i in text if i in 'уеёыаоэяию']
print(f'Список гласных букв: {letters}')
print(f'Длина списка: {len(letters)}')
