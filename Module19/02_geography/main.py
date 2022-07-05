global_dict = {}
country_num = int(input('Количество стран: '))
for i in range(country_num):
    country = input('{} страна: '.format(i + 1)).split()
    for town in country[1:]:
        global_dict[town] = country[0]
for i in range(1, 4):
    city = input('{} Город: '.format(i))
    if global_dict.get(city):
        print('Город {} расположен в стране {}'.format(city, global_dict[city]))
    else:
        print('По городу {} данных нет'.format(city))
