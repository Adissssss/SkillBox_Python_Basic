text = input('Введите строку: ')
cod = ''
n = 1
for i in range(len(text) - 1):
    if text[i] == text[i + 1]:
        n += 1
    if text[i] != text[i + 1] or i == len(text) - 2:
        cod += text[i] + str(n)
        n = 1
if text[-2] != text[-1]:
    cod += text[-1] + '1'
print('Закодированная строка:', cod)
