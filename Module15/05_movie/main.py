films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия'
         'Город грехов', 'Мементо', 'Отступники', 'Деревня']
N = int(input('Сколько фильмов хотите добавить? '))
film_list = []
for i in range(N):
    film = input(f'Введите название фильма: ')
    if film in films:
        film_list.append(film)
    else:
        print(f'фильма {film} у нас нет :(')
film_list_str = ','.join(map(str, film_list))
print(f'Ваш список люимых фильмов {film_list_str}')
