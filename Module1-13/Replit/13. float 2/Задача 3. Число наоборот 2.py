print('Задача 3. Число наоборот 2')


# Пользователь вводит два числа — N и K.
# Напишите программу,
# которая заменяет каждое число на число,
# которое получается из исходного записью его цифр в обратном порядке,
# затем складывает их,
# снова переворачивает и выводит ответ на экран.

# Пример:

# Введите первое число: 102
# Введите второе число: 123


# Первое число наоборот: 201
# Второе число наоборот: 321

# Сумма: 522
# Сумма наоборот: 225


def revers_num(num):
    countNum = num
    count, revers = 0, 0
    while countNum != 0:
        countNum //= 10
        count += 1
    while num != 0:
        digit = num % 10
        revers += digit * 10 ** (count - 1)
        num //= 10
        count -= 1
    return revers


x1 = int(input('Введите первое число: '))
x2 = int(input('Введите второе число: '))
print()
revX1 = revers_num(x1)
revX2 = revers_num(x2)
summ = revX1 + revX2
print(f'Первое число наоборот: {revX1}')
print(f'Второе число наоборот: {revX2}')
print()

print(f'Сумма: {summ}')
print(f'Сумма наоборот: {x1 + x2}')

# С задачей программа справляется =)

# N = int(input('Введите первое число: '))
# K = int(input('Введите второе число: '))
# print()
# # N, K = str(N), str(K)
# revN, revK = str(N)[::-1], str(K)[::-1]
# # summa1 = int(revN) + int(revK)
# print(f'Первое число наоборот: {revN}\nВторое число наоборот: {revK}')
# print()
# print(f'Сумма: {int(revN) + int(revK)}\nСумма наоборот: {N + K}')
