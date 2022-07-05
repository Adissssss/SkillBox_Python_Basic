n = int(input('Введите количество человек: '))
parents_tree = {}
for _ in range(1, n):
    pair = input(f'{_} пара: ').split()
    parents_tree[pair[0]] = pair[1]


def func(new_name):
    if new_name not in parents_tree:
        return 0
    else:
        return 1 + func(parents_tree[new_name])


heights = {}
for name in set(parents_tree.keys()) | set(parents_tree.values()):
    heights[name] = func(name)
print('Высота каждого члена семьи:')
for key, value in sorted(heights.items()):
    print(key, value)
