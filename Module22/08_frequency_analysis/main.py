from operator import itemgetter

freq = {}
n = 0
new_file = open('text.txt', 'r').read().lower()
for symbol in new_file:
    if ord('a') <= ord(symbol) <= ord('z'):
        x = freq.get(symbol, 0)
        freq[symbol] = x + 1
        n += 1
res = [(k, '{:5.3f}'.format(freq[k] / n)) for k in freq.keys()]
res = sorted(res, key=itemgetter(0))
res = sorted(res, key=itemgetter(1), reverse=True)
res = '\n'.join([i[0] + ' ' + i[1] for i in res])
print(res)
open('analysis.txt', 'w').write(res)
