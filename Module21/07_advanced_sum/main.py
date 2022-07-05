def summa(*args):
    return sum(summa(*arg) if isinstance(arg, list) else arg for arg in args)


lists = [1, 2, 3, [4], [[5]], 5]
print('Ответ: ', summa(lists))
