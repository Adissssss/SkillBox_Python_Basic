res = 0
file = open('people.txt', 'r', encoding='utf-8')
people_file = file.read().split('\n')
for i, line in enumerate(people_file):
    try:
        res += len(line.strip())
        if len(line) < 3:
            raise ValueError
    except ValueError:
        open('errors.log', 'a', encoding='utf-8').write(f'Строка {i + 1} - ValueError\n')
print(res)
file.close()
