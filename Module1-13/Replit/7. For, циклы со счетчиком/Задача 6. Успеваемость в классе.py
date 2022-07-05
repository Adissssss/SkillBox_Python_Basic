print('Задача 6. Успеваемость в классе')

# В классе N человек.
# Каждый из них получил за урок по информатике оценку: 3, 4 или 5, двоек сегодня не было.
#
# Напишите программу,
# которая получает список оценок - N чисел - и выводит на экран сообщение о том,
# кого сегодня больше: отличников, хорошистов или троечников.

count_3 = 0
count_4 = 0
count_5 = 0
N = int(input('enter number of student: '))
for i in  range(N):
  rate = int(input('enter students rating: '))
  if rate == 3:
    count_3 += 1
  elif rate == 4:
    count_4 += 1
  else:
    count_5 += 1
if count_4 < count_3 > count_5:
  print('there are more <bad> students today')
elif count_3 < count_4 > count_5:
  print('the are more <good> student today')
elif count_3 < count_5 > count_4:
  print('the are more <excellent> student today')

# elif count_3 == count_4 == count_5:
#    print('today the same number all student')
# elif count_3 == count_4 < count_5:
#   print('the are more <excellent> student today')
# elif count_3 == count_4 > count_5:
#   print('the are more <bad and good> student today')
# elif count_3 == count_5 < count_4:
#   print('the are more <excellent> student today')
# elif count_3 == count_5 > count_4:
#   print('the are more <bad and excellent> student today')
# elif count_4 == count_5 and count_4 == count_5 < count_3:
#   print('there are more <bad> students today')
# elif count_4 == count_5 and count_4 == count_5 > count_3:
#   print('there are more <good and excellent> students today')
# print(count_3, count_4, count_5)

