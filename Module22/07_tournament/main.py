from operator import itemgetter


result_list = (open("first_tour.txt", "r").read()).split('\n')
K = result_list[0]
winners = []

for player in result_list[1:]:
    if player.split()[2] > K:
        winner = (player.split()[1][0] + '. ' + player.split()[0], player.split()[2])
        winners.append(winner)

winners = sorted(winners, key=itemgetter(1), reverse=True)
open('second_tour.txt', 'a').write(str(len(winners)) + '\n')
print(len(winners))
for i, player in enumerate(winners):
    player = f'{i + 1}) {" ".join(player)}'
    open('second_tour.txt', 'a').write(player + '\n')
    print(player)
