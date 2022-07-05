print('Задача 2. Коллекторы')

# Напишите робота для коллекторов.
# В самом начале он спрашивает имя должника и сумму долга,
# а затем начинает требовать у него погашения до тех пор,
# пока он не введёт нужную сумму (равную сумме долга или больше).
# После погашения долга сообщите об этом пользователю и поблагодарите его.

# Пример:
# Василий, ваша задолженность составляет 100 рублей.
# Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? 50

# Маловато, Василий. Давайте ещё раз.
# Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? 90
# Маловато, Василий. Давайте ещё раз.

# Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? 110
# Отлично, Василий! Вы погасили долг. Спасибо!

name = input("..enter debtor's name: ")
debt = int(input('..enter amount of debt: '))
print(f'{name}, your debt is {debt} rubles! \n\nHow many rubles will you deposit right now to pay it off?')
deposit = int(input('..enter amount of deposit: '))
while deposit < debt:
    deposit = int(input(f'Do not kidding me! Give me my money, {name}!: '))
print(f'well done, {name}, but next time think about who to borrow money from!')




