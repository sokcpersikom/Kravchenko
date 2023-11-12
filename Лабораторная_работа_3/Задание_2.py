# Задание №2
def find_common_participants(first_group, second_group, splitter=','):
    first = first_group.split(splitter)
    second = second_group.split(splitter)
    result = list(set(first).intersection(set(second)))
    result.sort()
    return result
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
print(f"Общие участники: {find_common_participants(participants_first_group, participants_second_group, splitter='|')}")
#participants_first_group = "Иванов,Петров,Сидоров"
#participants_second_group = "Петров,Сидоров,Смирнов"
#print(f"Общие участники: {find_common_participants(participants_first_group, participants_second_group)}")

