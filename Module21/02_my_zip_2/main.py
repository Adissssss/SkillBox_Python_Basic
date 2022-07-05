def zipper(*args):
    return ((x[i] for x in args) for i in range(min(map(len, args))))



num = [1, 2, 3, 4, 5]
eng = {'a', 'b', 'c', 'd', 'e'}
rus = ('a', 'б', 'в', 'г', 'д')

result = zipper(num, eng, rus)
print(result)

for element in result:
    print(element)
