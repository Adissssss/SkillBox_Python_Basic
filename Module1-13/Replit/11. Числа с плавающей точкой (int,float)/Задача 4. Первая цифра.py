print('Задача 4. Первая цифра')

# Дано положительное действительное число X.
# Выведите его первую цифру после десятичной точки.
# При решении этой задачи нельзя пользоваться условной инструкцией, циклом или строками

x = float(input('Введите положительное действительное число: '))
x *= 10
x  = int(x % 10)
print(f'Первая цифра после десятичной точки: {x}')
