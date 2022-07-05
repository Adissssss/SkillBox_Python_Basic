players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}
players_tuple = list(i_name + i_score for i_name, i_score in players.items())
print('Ответ: ', players_tuple)
