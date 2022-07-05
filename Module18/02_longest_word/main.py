text = input('Введите строку: ').split(' ')
max_letter = text[0]
for i in range(1, len(text)):
    if len(text[i]) > len(max_letter):
        max_letter = text[i]
print('Самое длинное слово:', max_letter)
print('Длина слова:', len(max_letter))
