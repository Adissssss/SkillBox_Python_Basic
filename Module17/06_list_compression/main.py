nums = [1, 2, 0, 0, 3, -5, 8, 11, 0, 2]
for _ in range(nums.count(0)):
    nums.append(0)
    nums.remove(0)
for _ in range(nums.count(0)):
    nums.remove(0)
print(f'Финальный список: {nums}')
