"""
Пользователь вводит любые цифры через запятую
Сохранить цифры в список
Получить новый список в котором будут только уникальные элементы
исходного (уникальным считается символ, который встречается в исходном списке только 1 раз)
Вывести новый список на экран
"""
input_is_correct = True
my_str = input('Через запятую введите любые цифры: ')
my_list = list()
list_from_str = my_str.split(',')
for elem in list_from_str:
    if elem.isdigit():
        if not int(elem) in my_list: my_list.append(int(elem))
    else:
        if not elem in my_list: my_list.append(elem)
        input_is_correct = False
if not input_is_correct:
    print('Вообще-то я просила ввести цифры :(, ну да ладно:')
print(my_list)
