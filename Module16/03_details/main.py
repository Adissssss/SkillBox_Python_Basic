shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]
name_detail = input('Название детали: ')
count, symma = 0, 0
for element in shop:
    if name_detail in element:
        count += 1
        symma += element[1]
print(f'Количество деталей: {count}')
print(f'Общая стоимость: {symma}')
