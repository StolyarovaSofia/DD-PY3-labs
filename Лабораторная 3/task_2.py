# TODO Напишите функцию find_common_participants
def find_common_participants(p1, p2, separator =','):
    p_list1 = p1.split(separator)
    p_list2 = p2.split(separator)
    common_p = list(set(p_list1).intersection(p_list2))
    common_p.sort()

    return common_p

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
p = find_common_participants(participants_first_group,participants_second_group)
print(p)