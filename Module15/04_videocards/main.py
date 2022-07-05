N = int(input('Количество видеокарт: '))
graphics_card_list = []
new_graphics_card_list = []
max_graphics_card = 0
for i in range(1, N + 1):
    model = int(input(f'Видеокарта: '))
    graphics_card_list.append(model)
    if model > max_graphics_card:
        max_graphics_card = model
for model in graphics_card_list:
    if model != max_graphics_card:
        new_graphics_card_list.append(model)
print(f'Старый список видеокарт: {graphics_card_list}')
print(f'Новый список видеокарт: {new_graphics_card_list}')
