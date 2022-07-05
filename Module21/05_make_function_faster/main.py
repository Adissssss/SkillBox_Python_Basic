def calculating_math_func(data, fact_dict=None):
	if fact_dict is None:
		fact_dict = {}
	assert data >= 0, 'Факториал отрицательных чисел считается иначе!'
	if data in fact_dict:
		result = fact_dict[data]
	else:
		result = 1
		for index in range(1, data + 1):
			result *= index
		fact_dict[data] = result
	result /= data ** 3
	result = result ** 10
	return result


number = int(input('Введите число: '))
new_result = calculating_math_func(number)
print('Ответ: ', new_result)
