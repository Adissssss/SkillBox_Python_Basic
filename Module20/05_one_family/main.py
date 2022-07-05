database = {
        'Сидоров Алексей': 35,
        'Сидорова Алена': 30,
        'Сидоров Ян': 20,
        'Иванов Петр': 40,
        'Иванова Галя': 36,
        'Иванова Света': 24
}

search = input('Введите фамилию в именительном падеже: ').lower()


for i_name, i_age in database.items():
        res = i_name.split()
        if search == res[0].lower() or search == res[0][:-1].lower():
                print(i_name, i_age)







