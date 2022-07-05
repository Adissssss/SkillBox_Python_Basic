def fibo(number):
    n1 = n2 = 1
    if number in (1, 2):
        return 1
    for i in range(2, number):
        n1, n2 = n2, n1 + n2
    return n2


num_pos = int(input('Введите позицию числа в ряде Фибоначчи: '))
print(fibo(num_pos))