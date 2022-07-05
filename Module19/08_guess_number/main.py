n = int(input('Введите максимальное число: '))
all_nums = set(range(1, n + 1))
possible_nums = all_nums
while True:
    guest = input('Нужное число есть среди вот этих чисел: ').lower()
    if guest == 'помогите!':
        break
    guest = set(int(x) for x in guest.split())
    leader = input('Ответ "да" или "нет": ').lower()
    if leader == 'да':
        possible_nums &= guest
    else:
        possible_nums &= all_nums - guest
nums = ' '.join([str(x) for x in sorted(possible_nums)])
print('Артём мог загадать следующие числа:', nums)
