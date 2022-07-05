import random

res_dict = []
num_list = [random.randint(0, 100) for x in range(10)]
print('Оригинальный список: ', num_list)

for index, num in enumerate(num_list):
    if index % 2 != 0:
        res_dict.append((num_list[index - 1], num))

print('Новый список: ', res_dict)
