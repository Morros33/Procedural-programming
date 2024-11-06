# TODO Напишите функцию find_common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

def find_common_participants(group_1, group_2, sep):
    set_group_1 = set(group_1.split(sep))
    set_group_2 = set(group_2.split(sep))
    common_participants = set_group_1.intersection(set_group_2)
    common_participants = list(common_participants)
    common_participants.sort()
    return(common_participants)

print(find_common_participants(participants_second_group, participants_first_group, "|"))




# TODO Провеьте работу функции с разделителем отличным от запятой
