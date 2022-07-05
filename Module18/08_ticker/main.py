first_line = input('Первая строка: ')
second_line = input('Вторая строка: ')
count = len(first_line)
result = 0
for i in range(0, count):
    x = ''
    for j in range(0, count):
        x += first_line[(i + j) % count]
    if x == second_line:
        print('Первая строка получается из второй со сдвигом', i)
        result += 1
        break
if result == 0:
    print('Первую строку нельзя получить из второй с помощью циклического сдвига.')
