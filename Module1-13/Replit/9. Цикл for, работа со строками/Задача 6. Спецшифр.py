print('Задача 6. Спецшифр')

# Два сотрудника спецслужб переписываются необычным шифром.
# Каждую букву они шифруют в виде строки,
# внутри которой есть длинная последовательность букв “s”,
# а длина самой длинной - это и есть номер буквы алфавита, которую хотят отправить.
#
# Напишите программу,
# которая получает на вход строку,
# подсчитывает в ней самую длинную последовательность подряд идущих букв “s” и выводит ответ на экран.
#
# Пример:
# Введите строку: ssbbbsssbc
# Самая длинная последовательность: 3




text = input('введите строку: ')
# text = 'ssssssssssssasdadadssssssssss'
count, s_count = 0, 0
for symbol in text:
  if symbol == 's':
    count += 1
  if symbol != 's':
    count = 0
  elif s_count < count:
    s_count = count
  # print(count, end = ' ')


print(s_count)



