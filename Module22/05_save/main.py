import os.path


def re_write_file(text, new_path):
    with open(new_path, 'w', encoding='utf-8') as file:
        file.write(text)
        print('Файл успешно перезаписан!')
    with open(new_path, 'r', encoding='utf-8') as file:
        print(f'\nСодержимое файла: \n{file.read()}')
        return


def write_file(text, new_path):
    with open(new_path, 'w', encoding='utf-8') as file:
        file.write(text)
        print('Файл успешно сохранен!')
    with open(new_path, 'r', encoding='utf-8') as file:
        print(f'\nСодержимое файла: \n{file.read()}')
        return


user_text = input('Введите что-нибудь: ')
while True:
    user_path = input('Куда хотите сохранить документ? '
                      'Введите последовательность папок (через пробел):\n').split()
    path = os.path.abspath(os.path.join('/', *user_path))
    if not os.path.isdir(path):
        print('Введите корректный путь.')
    else:
        file_name = input('Введите имя файла:\n')
        file_path = os.path.abspath(os.path.join(path, file_name))
        if file_name is os.listdir(path):
            print('Перезаписать файл? да/нет')
            answer = input().lower()
            if answer == 'да':
                re_write_file(user_text, file_path)
                break
            elif answer == 'нет':
                break
        else:
            write_file(user_text, file_path)
            break
