users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

users_2 = set(users)

dict_users = {
    "Общее количество": 0,
    "Уникальные посещения": 0,
}

dict_users["Общее количество"] += len(users)
dict_users["Уникальные посещения"] += len(users_2)

print(dict_users)
# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
