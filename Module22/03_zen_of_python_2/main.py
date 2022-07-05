import os


def lines_count(new_file):
    line_count = len(new_file.split('\n'))
    return line_count


def words_count(new_file):
    word_count = 0
    for symbol in new_file.title():
        if symbol.isupper():
            word_count += 1
    return word_count


def letters_count(new_file):
    letter_count = 0
    for symbol in new_file:
        if symbol.isalpha():
            letter_count += 1
    return letter_count


def rare_letter(new_file):
    letter_dict = {}
    for symbol in new_file.lower():
        if symbol.isalpha():
            if symbol in letter_dict:
                letter_dict[symbol] = letter_dict[symbol] + 1
            else:
                letter_dict[symbol] = 1
    return min(letter_dict, key=lambda x: letter_dict[x])


abs_path = os.path.abspath((os.path.join('..', '02_zen_of_python', 'zen.txt')))
file = open(abs_path, 'r')
data = file.read()
file.close()

print('Количество строк: ', lines_count(data))
print('Количество слов: ', words_count(data))
print('Количество букв: ', letters_count(data))
print('Минимально встречающаяся буква: ', rare_letter(data))
