site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        },
        'http': {
            'web': {
                'head': 'h1'
            }
        },
        'ewq': {
            '2r': 'zc',
            'q1': 'vc',
            'w2': 'bv'
        }
    }
}


def find_key(struct, key, depth):
    if depth == 0:
        return None
    elif key in struct:
        return struct[key]

    for sub_struct in struct.values():
        if isinstance(sub_struct, dict):
            result = find_key(sub_struct, key, depth - 1)
            if result:
                break
    else:
        result = None
    return result


user_key = input('Введите ключ: ')
depth_user = int(input('Введите глубину поиска: '))
value = find_key(site, user_key, depth_user)
if value:
    print('Значение ключа: ', value)
elif value is None:
    print('Превышена глубина!')
else:
    print('Такого ключа нет')
