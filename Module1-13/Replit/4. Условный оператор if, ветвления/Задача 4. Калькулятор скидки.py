print('Задача 4. Калькулятор скидки')

# Андрей переехал на новую квартиру, и ему нужно купить три стула в разные комнаты.
# Естественно, цена на стулья в разных магазинах различается,
# а где-то ещё и скидка есть.
# Вот для одного из таких магазинов он и написал калькулятор скидки,
# чтобы проще ориентироваться в ценах.

# Напишите программу,
# которая запрашивает три стоимости товара и вычисляет сумму чека.
# Если сумма чека превышает 10 000 рублей,
# то нужно вычесть из этой суммы скидку 10% (умножить на 10, разделить на 100).
# В конце вывести итоговую сумму на экран.

price1 = int(input('price of product 1: '))
price2 = int(input('price of product 2: '))
price3 = int(input('price of product 3: '))
sum_price = price1 + price2 + price3

if sum_price > 10000:
    sum_price = sum_price - sum_price * 0.1
    print('discounted amount = ', sum_price)
else:
    print('total amount = ', sum_price)
