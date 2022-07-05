def reverse_number(number):
    intDig, fractDig, dig, fract = '', '', '', ''
    x = str(number)
    for i in x:
        fractDig = i + fractDig
        if i != '.':
            dig = i + dig
        elif i == '.':
            intDig = dig
            fractDig = fract
    result = intDig + '.' + fractDig
    return float(result)


number1 = float(input('Введите первое число: '))
number2 = float(input('Введите второе число: '))
print()
number1 = reverse_number(number1)
number2 = reverse_number(number2)

print(f'Первое число наоборот: {number1}')
print(f'Второе число наоборот: {number2}')
print(f'Сумма: {number1 + number2}')
