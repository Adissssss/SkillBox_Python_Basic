with open('zen.txt', 'r') as file:
    for text in reversed(file.readlines()):
        print(text, end='')
