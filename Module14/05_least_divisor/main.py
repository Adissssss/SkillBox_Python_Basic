def nd(num):
    min_del = 0
    for i in range(2, num + 1):
        if num % i == 0:
            min_del = i
            break
    return min_del


number = int(input('Введите число: '))
if number > 1:
    nd = nd(number)
    print(f'Наименьший делитель, отличный от единицы: {nd}')
else:
    print('Введите натуральное число n >1')
