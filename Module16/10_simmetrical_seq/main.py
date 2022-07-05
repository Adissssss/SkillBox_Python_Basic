def is_palindrome(num_list):
    reverse_list = []
    for i_num in range(len(num_list) - 1, -1, -1):
        reverse_list.append(num_list[i_num])
    if num_list == reverse_list:
        return True
    else:
        return False


N = int(input('Количество чисел: '))
sequence_list = []
for _ in range(1, N + 1):
    number = int(input('Число: '))
    sequence_list.append(number)
print(f'Последовательность: {sequence_list}')
new_sequence_list = []
answer = []
for i in range(0, len(sequence_list)):
    for j in range(i, len(sequence_list)):
        new_sequence_list.append(sequence_list[j])
    if is_palindrome(new_sequence_list):
        for i_answer in range(0, i):
            answer.append(sequence_list[i_answer])
        answer.reverse()
        break
    new_sequence_list = []
print('Исходный список:', sequence_list)
print('Нужно чисел для полиндрома: ', len(answer))
print('Список этих чисел', answer)
