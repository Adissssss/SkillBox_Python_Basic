N = int(input('Введите длину списка: '))
new_list = [1 if x % 2 == 0 else x % 5 for x in range(N)]
print(f'Результат: {new_list}')
