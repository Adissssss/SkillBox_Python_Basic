print('Задача 3. Посчитай чужую зарплату...')

# Бухгалтер устала постоянно считать вручную среднегодовую зарплату сотрудников компании
# и, чтобы облегчить себе жизнь, обратилась к программисту.

# Напишите программу,
# которая принимает от пользователя зарплату сотрудника за каждый из 12 месяцев
# и выводит на экран среднюю зарплату за год.


cash = 0
for month in range(1, 13):
    salary = int(input(f'salary for {month} month: '))
    cash += salary
print(f'average salary for the year: {cash / 12} USD')