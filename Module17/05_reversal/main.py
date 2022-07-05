line = input('Введите строку с двумя буквами h: ')
print('Ответ: ', (line[:line.index('h') + 1:]) + line[line.rindex('h') - 1:line.index('h'):-1] +
      (line[line.rindex('h'):]))
