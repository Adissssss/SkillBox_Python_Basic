numbers_file = open('numbers.txt', 'r')
result = 0
for i_line in numbers_file:
    for element in i_line:
        if element.isdigit():
            result += int(element)
result_file = open('answer.txt', 'w')
result_file.write(str(result))
numbers_file.close()
result_file.close()
