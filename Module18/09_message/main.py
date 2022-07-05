text = 'Хотя, возмо:жно и нет'
rev_text, letter = '', ''
for symbol in text:
    if symbol.isalpha():
        letter += symbol
    else:
        rev_text += letter[::-1] + symbol
        letter = ''
else:
    rev_text += letter[::-1]
print('Результат:', rev_text)
