from datetime import datetime

user_name = input('Введите имя пользователя: ')
print(f'{user_name} подключился к чату.')
while True:
    print('Посмотреть чат - 1\nНаписать сообщение - 2\nВыйти из чата - 3')
    answer = input('Ваш выбор: ')
    if answer == '1':
        try:
            with open('chat.txt', 'r', encoding='utf-8') as chat:
                log_chat = chat.readlines()
                print(''.join(log_chat))
        except FileNotFoundError:
            print('Такого чата нет.')
    elif answer == '2':
        message = f'{datetime.now()} {user_name}: {input("Введите сообщение: ")}\n'
        with open('chat.txt', 'a', encoding='utf-8') as chat:
            chat.write(message)
    elif answer == '3':
        print(f'{user_name} покинул чат.')
        break
    else:
        print('Что-то пошло не так :(')



