num = 0
big_letter = 0
while True:
    password = input('Придумайте пароль: ')
    for i in range(len(password)):
        if password[i].isdigit():
            num += 1
    for i in range(len(password)):
        if password[i].isupper():
            big_letter += 1
    if num < 3 or big_letter < 1 or len(password) < 8:
        print('Пароль ненадёжный. Попробуйте ещё раз.')
    else:
        print('Это надёжный пароль!')
        break
