def summa_n(n):
    summa = 0
    while n != 0:
        digit = n % 10
        summa += digit
        n //= 10
    print(f'Сумма цифр: {summa}')
    return summa


def number_n(n):
    count = 0
    while n > 0:
        count += 1
        n //= 10
    print(f'Количество цифр в числе: {count}')
    return count


n1 = int(input('Введите число: '))
if n1 > 0:
    x1 = summa_n(n1)
    x2 = number_n(n1)
    x3 = x1 - x2
    print(f'Разность суммы и количества: {x3}')
else:
    print('Введите целое положительное число')
