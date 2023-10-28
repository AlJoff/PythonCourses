def find_common_participants(first_participants, second_participants, separator=","):
    list_first_participants = first_participants.split(separator)
    list_second_participants = second_participants.split(separator)

    list_common_participants = list(set(list_first_participants).intersection(list_second_participants))
    list_common_participants.sort()
    return list_common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print('Cписок общих участников:', find_common_participants(participants_first_group, participants_second_group, "|"))
