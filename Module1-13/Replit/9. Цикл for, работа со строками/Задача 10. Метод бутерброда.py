print('Задача 10. Метод бутерброда')

# Секретное агентство «Super-Secret-no» решило
# для шифрования переписки своих сотрудников использовать «метод бутерброда».
# Сначала буквы слова нумеруются в таком порядке:
# первая буква получает номер 1,
# последняя буква - номер 2,
# вторая – номер 3,
# предпоследняя – номер 4, потом третья … и так для всех букв (см. рисунок).
# Затем все буквы записываются в шифр в порядке своих номеров.
#
# Например, слово «sandwich» зашифруется в «shacnidw».
#
# К сожалению, программист «Super-Secret-no», написал только программу шифрования и уволился.
# И теперь агенты не могут понять, что же они написали друг другу. Помогите им.
#
# Пример:
# Введите зашифрованное сообщение: shacnidw
# Расшифрованное сообщение: sandwich
#          1   3   5   7   8   6   4   2
# Слово: | s | a | n | d | w | i | c | h |
#
# Шифр:  | s | h | a | c | n | i | d | w |

# var #1
code = 'shacnidw'
decode1 = ''
decode2 = ''
count = 0
for symbol in code:
    count += 1
    if count % 2 != 0:
        decode1 += symbol
    if count % 2 == 0:
        decode2 = symbol + decode2
        # print(count, symbol, end = ' ')
count = 0

print(decode1 + decode2)

# var #2
# code = 'shacnidw'
# decode = ''
# count = 0
# for symbol in code:
#   count += 1
#   if count % 2 != 0:
#     decode += symbol
# count = 0
# for symbol in reversed(code):
#   count += 1
#   if count % 2 != 0:
#     decode += symbol

# print(decode)

