def funct(checking_list):
    return [sym for i, sym in enumerate(checking_list) if is_prime(i)]


def is_prime(num):
    k = 0
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            k += 1
    if k == 0 and num > 1:
        return True
    else:
        return False


text = input('Введите текст: ')
print('Ответ: ', funct(text))
