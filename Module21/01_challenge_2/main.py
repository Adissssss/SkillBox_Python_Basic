def all_number(number):
    if number == 1:
        print(number, end=' ')
        return
    all_number(number - 1)
    print(number, end=' ')


num = int(input('Введите число: '))
all_number(num)