print('Задача 6. Маятник ')

# Известно, что амплитуда качающегося маятника с каждым разом затухает
# на 8,4% от амплитуды прошлого колебания.
# Если качнуть маятник,
# то, строго говоря, он не остановится никогда,
# просто амплитуда будет постоянно уменьшаться до тех пор,
# пока мы не сочтём такой маятник остановившимся.

# Напишите программу,
# определяющую, сколько раз качнётся маятник, прежде чем он, по нашему мнению, остановится.

# Программа получает на вход
# начальную амплитуду колебания в сантиметрах
# и конечную амплитуду его колебаний,
# которая считается остановкой маятника.

# Обеспечьте контроль ввода.

# Пример:

# Введите начальную амплитуду: 1
# Введите амплитуду остановки: 0.1

# Маятник считается остановившимся через 27 колебаний


beginAmp = int(input('Введите начальную амплитуду: '))
endAmp = float(input('Введите амплитуду остановки: '))
amp_count = 0
while beginAmp > endAmp:
    amp_count += 1
    beginAmp = beginAmp - (beginAmp * 0.084)
print(f'Маятник считается остановившимся через {amp_count} колебаний')


