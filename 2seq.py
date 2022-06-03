"""
Пользователь вводит любые цифры через запятую
Сохранить цифры в список
Получить новый список в котором будут только уникальные элементы
исходного (уникальным считается символ, который встречается в исходном списке только 1 раз)
Вывести новый список на экран
"""
input_is_correct = True
list_sep_ch = [',', '/', ';']
sep_ch = input('Задайте символ-разделитель (",", ";", "/") для элементов списка: ')
if sep_ch not in list_sep_ch:
    print('Задан некорректный разделитель элементов списка')
else:
    my_str = input('Через {0} введите любые цифры: '.format(sep_ch))
    my_list = list()
    list_from_str = my_str.split(sep_ch)
    for elem in list_from_str:
        if elem.isdigit():
            if not int(elem) in my_list: my_list.append(int(elem))
        else:
            if not elem in my_list: my_list.append(elem)
            input_is_correct = False
    if not input_is_correct:
        print('Вообще-то я просила ввести цифры :(, ну да ладно:')
    print(my_list)
