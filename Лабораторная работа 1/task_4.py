users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
siteVisitStatistics = {
    "Общее количество": 0,
    "Уникальные посещения": 0
}

siteVisitStatistics["Общее количество"] = len(users)
siteVisitStatistics["Уникальные посещения"] = len(set(users))

print(siteVisitStatistics)
