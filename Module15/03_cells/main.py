N = int(input('Количество клеток: '))
cell_list = []
remoted_cell = []
for i in range(N):
    cell = int(input(f'Значение клетки {i + 1} - '))
    cell_list.append(cell)
    if i > cell_list[i]:
        remoted_cell.append(cell_list[i])
remoted_cell_str = ','.join(map(str, remoted_cell))
print(f'Неподходящие значения: {remoted_cell_str}')
