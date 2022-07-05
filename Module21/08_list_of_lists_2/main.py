def list_rev(new_list):
    if not new_list:
        return new_list
    for i, element in enumerate(new_list):
        if isinstance(element, list):
            return list_rev(element) + list_rev(new_list[i + 1:])
        else:
            return [element] + list_rev(new_list[i + 1:])


lists = [1, 2, [3, 4], [4], [[5]], [[[[7]]]], [], 9]
print('Ответ: ', list_rev(lists))
