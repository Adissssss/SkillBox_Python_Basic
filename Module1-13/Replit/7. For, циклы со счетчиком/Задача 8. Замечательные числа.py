print('Задача 8. Замечательные числа')

#Напишите программу,
# которая находит и выводит все двузначные числа,
# которые равны утроенному произведению своих цифр.
# К таким относятся, например, 15 и 24.

for i in range(10, 100):
  a = i % 10
  b = i // 10
  if i == (a * b) * 3:
    print(i)