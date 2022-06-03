"""
Пользователь вводит элементы 1-го списка (по очереди как в МОДУЛЬ 1 или вместе как в МОДУЛЬ 2)
Затем он вводит элементы 2-го списка
Удалить из первого списка элементы присутствующие во 2-ом и вывести результат на экран
"""
my_list = list()
sep_ch = ','
list_from_str_1 = input('Через запятую введите элементы первого списка: ').split(sep_ch)
list_from_str_2 = input('Через запятую введите элементы второго списка: ').split(sep_ch)
for elem in list_from_str_2:
    if elem in list_from_str_1:
        for i in range(list_from_str_1.count(elem)): list_from_str_1.remove(elem)
for elem in list_from_str_1:
    if elem.isdigit():
        my_list.append(int(elem))
    else:
        my_list.append(elem)
print(my_list)