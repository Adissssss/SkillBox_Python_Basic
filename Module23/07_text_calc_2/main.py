def string_validation(string):
    operators = ['+', '-', '*', '/', '//', '%']
    expression = string.split()
    x1, x2, operator = expression[0], expression[2], expression[1]
    if len(expression) == 3 and x1.isdigit() and x2.isdigit() and operator in operators:
        return True
    else:
        if len(expression) != 3:
            raise IndexError('Не корректное выражение')
        elif not x1.isdigit() or not x2.isdigit():
            raise ValueError('Не корректные операнды')
        elif operator not in operators:
            raise SyntaxError('Неизвестный оператор')


def calc_string(string):
    expression = string.split()
    x1, x2, operator = int(expression[0]), int(expression[2]), expression[1]
    if operator == '+':
        return x1 + x2
    elif operator == '-':
        return x1 - x2
    elif operator == '*':
        return x1 * x2
    elif operator == '/':
        return x1 / x2
    elif operator == '//':
        return x1 // x2
    elif operator == '%':
        return x1 % x2


sym = 0
with open('calc.txt', 'r', encoding='utf-8') as arithmetic:
    arithmetic = arithmetic.read().split('\n')
    for line in arithmetic:
        while True:
            try:
                if string_validation(line):
                    result = calc_string(line)
                    sym += result
                break
            except (IndexError, ValueError, SyntaxError) as error:
                print(f'В строке {line} обнаружена ошибка. {error}.')
                answer = input('Исправить? да/нет\n').lower().strip()
                if answer == 'да':
                    line = input('Введите исправленную строку: ').strip()
                elif answer == 'нет':
                    break
                else:
                    print('неизвестная команда.')
    print(f'Сумма всех выражений: {sym}')
