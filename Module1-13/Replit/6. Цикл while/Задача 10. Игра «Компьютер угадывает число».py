print('Задача 10. Игра «Компьютер угадывает число»')

# Поменяйте мальчика и компьютер из прошлой задачи местами.
# Теперь мальчик загадывает число между 1 и 100 (включительно).
# Компьютер может спросить у мальчика:
# «Твое число равно, меньше или больше, чем число N?»,
# где N — число, которое хочет проверить компьютер.
# Мальчик отвечает одним из трёх чисел:
# 1 — равно,
# 2 — больше,
# 3 — меньше.

# Напишите программу,
# которая с помощью цепочки таких вопросов и ответов мальчика угадывает число.

# Дополнительно: сделайте так, чтобы можно было гарантированно угадать число за семь попыток.

# num = int(input('guess the number from 1 to 100: '))
# N = 50
# while N > 0:
#   print(f'your number is more or less than {N}?')
#   response = int(input('1 - equal, 2 - more, 3 - less    '))
#   if response == 1:
#     print(f'guessed! Number - {N}')
#     break
#   elif response == 2:    # more
#     N += 1
#   elif response == 3:     # less
#     N -= 1

a = 1
b = 100
while True:
    N = (a + b) // 2
    print(f'Your number is: {N}?')
    response = int(input('1 - equal, 2 - more, 3 - less    '))
    if response == 1:
        print(f'guessed! Number - {N}')
        break
    elif response == 2:
        a = N + 1
    elif response == 3:
        b = N - 1