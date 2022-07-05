def shifer_cezarya(file_name):
    file = open('message.txt', 'r')
    data = file.read()
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    key = 0
    for line in data.split('\n'):
        key += 1
        cipher = ''
        for symbol in line.lower():
            symbol = alpha[alpha.index(symbol) + key % 26]
            cipher += symbol
        open('cipher_text.txt', 'a').write(cipher + '\n')
    print(f"Содержимое файла message.txt: \n{open('message.txt', 'r').read()}")
    print(f"Содержимое файла cipher_text.txt: \n{open('cipher_text.txt', 'r').read()}")
    file.close()


shifer_cezarya('message.txt')
