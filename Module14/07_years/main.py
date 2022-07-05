def relevant_years(first_year, second_year):
    for year in range(first_year, second_year + 1):
        d4 = year % 10
        d3 = (year // 10) % 10
        d2 = (year // 100) % 10
        d1 = year // 1000
        if d1 == d2 and d2 == d3 and d3 != d4:
            print(year)
        elif d1 == d2 and d2 == d4 and d4 != d3:
            print(year)
        elif d1 == d3 and d3 == d4 and d4 != d2:
            print(year)
        elif d2 == d3 and d3 == d4 and d4 != d1:
            print(year)


year1 = int(input('Введите первый год: '))
year2 = int(input('Введите второй год: '))
print(f'Года от {year1} до {year2} с тремя одинаковыми цифрами:')
relevant_years(year1, year2)
