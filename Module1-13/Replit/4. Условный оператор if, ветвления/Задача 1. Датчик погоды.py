print('Задача 1. Датчик погоды')

# В квартире стоит датчик погоды за окном
# , который определяет, идёт дождь или нет.
# Если пошёл дождь, датчик оповещает владельцев сообщением: «Пошёл дождь. Возьмите зонтик!»
# Напишите программу,
# которая получает на вход число 0 или 1.
# Единица означает, что дождь идёт.
# Если дождь идёт, то выводите на экран сообщение: «Пошёл дождь. Возьмите зонтик!».

# Пример:
# На улице идёт дождь? 1
# Пошёл дождь. Возьмите зонтик!

# Пример 2:
# На улице идёт дождь? 0
# Дождя нет =)
print("It's raining?")
sensor_output = int(input('     sensor singnal..'))

if sensor_output == 0:
  print('There is no rain.')
if sensor_output == 1:
  print("It's raining now!")

