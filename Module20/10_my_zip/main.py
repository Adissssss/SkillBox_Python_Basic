syms = 'abcd'
nums = (10, 20, 30, 40, 50)
zipped = ((syms[i], nums[i]) for i in range(min(len(syms), len(nums))))
print(zipped)
for element in zipped:
    print(element)
