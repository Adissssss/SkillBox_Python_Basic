def palindrom(new_string):
    symbol_count = {}
    for symbol in new_string:
        symbol_count[symbol] = symbol_count.get(symbol, 0) + 1
    odd_count = 0
    for value in symbol_count.values():
        if value % 2 != 0:
            odd_count += 1
    return odd_count <= 1


string = input('Введите строку: ')
if palindrom(string):
    print('Можно сделать полиндромом')
else:
    print('Нельзя сделать полиндромом')
