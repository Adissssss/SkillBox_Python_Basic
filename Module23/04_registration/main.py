def check_user(string):
    new_user_list = string.split()
    name = new_user_list[0]
    email = new_user_list[1]
    age = int(new_user_list[2])
    if not len(new_user_list) == 3:
        raise IndexError('НЕ присутствуют все три поля: IndexError.')
    elif not name.isalpha():
        raise NameError('Поле имени содержит НЕ только буквы: NameError.')
    elif '@' not in email or '.' not in email:
        raise SyntaxError('Поле «Имейл» НЕ содержит @ или .(точку): SyntaxError.')
    elif age < 10 or age > 99:
        raise ValueError('Поле «Возраст» НЕ является числом от 10 до 99: ValueError.')
    else:
        good_log.write(string + '\n')


user_file = open('registrations.txt', 'r', encoding='utf-8')
good_log = open('registrations_good.log', 'a', encoding='utf-8')
bad_log = open('registrations_bad.log', 'a', encoding='utf-8')
bad_log.write(f'№ строки       Данные                                                 Ошибка')
user_list = user_file.read().split('\n')
for i, line in enumerate(user_list):
    try:
        check_user(line)
    except (IndexError, NameError, SyntaxError, ValueError) as err:
        bad_log.write(f'\n{i + 1}         {line}                           {err}')

user_file.close()
good_log.close()
bad_log.close()
