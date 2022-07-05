num = 0
bad_count = 0
while True:
    ip = input('Введите IP: ').split('.')
    if len(ip) != 4:
        print('Адрес - это четыре числа, разделённые точками')
    else:
        for x in ip:
            if x.isdigit():
                num += 1
                if int(x) > 255 or int(x) < 0:
                    bad_count += 1
                    print(x, '- Введите число от 0 до 255')
            else:
                print(x, '- не целое число')
        if num == 4 and bad_count == 0:
            print('IP-адрес корректен')
            break
