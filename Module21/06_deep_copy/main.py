import copy


def rename_site(struct, name):
    for key, value in struct.items():
        if isinstance(value, str):
            if 'телефон' in value:
                struct[key] = value.replace('телефон', name)
        else:
            if isinstance(value, dict):
                rename_site(value, name)
    return struct


def add_site(full_struct, struct, name):
    full_struct[name] = rename_site(copy.deepcopy(struct), name)
    return full_struct


def print_struct(struct, space='  '):
    for key, value in struct.items():
        if not isinstance(value, dict):
            print(space, value)
        else:
            print(space, key)
            print_struct(value, space * 2)
            print()


site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на телефон',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}
data = {}
number_sites = int(input('Сколько сайтов: '))
for _ in range(number_sites):
    product_name = input('Введите название продукта для нового сайта: ')
    add_site(data, site, product_name)
    print_struct(data)
