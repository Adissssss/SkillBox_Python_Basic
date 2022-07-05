def tuple_sort(new_tuple):
    for element in new_tuple:
        if not isinstance(element, int):
            return new_tuple
    return tuple(sorted(new_tuple))


any_tuple = (5, 2, 4, 'h', 8)
print('Ответ: ', tuple_sort(any_tuple))
