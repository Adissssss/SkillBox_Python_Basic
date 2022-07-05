nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
final_nice_list = [x3 for x1 in nice_list for x2 in x1 for x3 in x2]
print('Ответ:', final_nice_list)
