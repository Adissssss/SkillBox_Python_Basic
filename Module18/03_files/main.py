name_file = input('Название файла:')
if name_file[0] in '@№$%^&*()':
    print('Ошибка: название начинается на один из специальных символов.')
elif not name_file.endswith('.txt') and not name_file.endswith('.docx'):
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx')
else:
    print('Файл назван верно.')
