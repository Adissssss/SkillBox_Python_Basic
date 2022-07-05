print('Задача 8. Вклады')

# Вклад в банке составляет X рублей.
# Ежегодно он увеличивается на P процентов,
# после чего дробная часть копеек отбрасывается.

# Определите, через сколько лет вклад составит не менее Y рублей.

# Напишите программу,
# которая по данным числам X, Y, P определяет,
# сколько лет пройдёт, прежде чем сумма достигнет значения Y.


deposit = int(input('enter amount of deposit: '))
needed_amount = int(input('what amount do you need?: '))
percentage_rate = int(input('enter the percentage rate in your bank: '))
years_count = 0
while deposit < needed_amount:
  deposit += (deposit * (percentage_rate / 100))
  years_count += 1
print(f'the required amount will be in {years_count} years')



