word = input('Введите слово: ')
word_list = list(word)
reverse_word_list = []
for i in range(len(word_list)):
    reverse_word_list.append(word_list[len(word_list) - i - 1])
print(reverse_word_list)


if word_list == reverse_word_list:
    print('Слово является палиндромом')
else:
    print('Слово не является палиндромом')
