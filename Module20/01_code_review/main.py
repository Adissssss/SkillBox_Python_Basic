students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }

}

for i_num, i_name in students.items():
    print('ID студента - ', i_num, 'возраст: ', i_name['age'])


def funct(dict1):
    interests_list, count = [], 0
    for i_num, i_name in dict1.items():
        interests_list.extend(i_name['interests'])
        count += len(i_name['surname'])
    return interests_list, count


interests = ', '.join(funct(students)[0])
lenght = funct(students)[1]
print('Интересы студентов: {}\nОбщая длина всех фамилий: {}'.format(interests, lenght))
