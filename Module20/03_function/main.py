def funct(new_tuple, elem):
    if elem in new_tuple:
        if new_tuple.count(elem) > 1:
            first_index = new_tuple.index(elem)
            second_index = new_tuple.index(elem, first_index + 1) + 1
            return new_tuple[first_index:second_index]
        else:
            return new_tuple[new_tuple.index(elem):]
    else:
        return ()


element = input('Введите элемент: ')
any_tuple = tuple(input('Введите кортеж: '))
print('Ответ: ', funct(any_tuple, element))
