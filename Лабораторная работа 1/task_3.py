list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
count_players = len(list_players)    # Количество игроков
middle_index = int(count_players/2)  # Индекс игрока по середине списка

print(list_players[:middle_index])
print(list_players[middle_index:])
