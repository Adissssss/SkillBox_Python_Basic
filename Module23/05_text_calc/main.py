def validation_line(string):
    operators = ['+', '-', '*', '/', '//', '%']
    line = string.split()
    if len(line) != 3:
        raise IndexError
    elif not line[0].isdigit() and line[2].isdigit:
        raise ValueError
    elif line[1] not in operators:
        raise SyntaxError
    else:
        return True


def calc_string(x1, x2, operation):
    if operation == '+':
        return x1 + x2
    elif operation == '-':
        return x1 - x2
    elif operation == '*':
        return x1 * x2
    elif operation == '/':
        return x1 / x2
    elif operation == '//':
        return x1 // x2
    elif operation == '%':
        return x1 % x2


sym = 0
with open('calc.txt', 'r') as arithmetic:
    arithmetic = arithmetic.read().split('\n')
    for i, line in enumerate(arithmetic):
        try:
            if validation_line(line):
                expression = line.split()
                operand_1 = int(expression[0])
                operand_2 = int(expression[2])
                operator = expression[1]
                result = calc_string(operand_1, operand_2, operator)
                sym += result
                print(f'{i + 1} выражение ({line}) равно: {result}')
        except IndexError:
            print('Не корректное значение')
        except ValueError:
            print('Не корректные операнды')
        except SyntaxError:
            print('Неизвестный оператор')
    print(f'Сумма всех выражений: {sym}')
