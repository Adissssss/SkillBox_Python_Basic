count = int(input('Введите количество пар слов: '))
text_dict = dict()
for i in range(1, count + 1):
    text = input(f'{i} пара: ').lower().split(' - ')
    text_dict[text[0]] = text[1]
    text_dict[text[1]] = text[0]
print(text_dict)
while True:
    word = input('Введите слово: ').lower()
    if word in text_dict:
        print('Синоним: {}'.format(text_dict[word]))
    else:
        print('Такого слова в словаре нет.')

