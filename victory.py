"""
Написать или улучшить программу Викторина из предыдущего дз
Есть 10 известных людей и их даты рождения в формате '02.01.1988' ('dd.mm.yyyy') - предлагаю
для тренировки пока использовать строку
Программа выбирает из этих 10-и 5 случайных людей, это можно реализовать с помощью модуля random
и функции sample
После того как выбраны 5 случайных людей, предлагаем пользователю ввести их дату рождения
пользователь вводит дату в формате 'dd.mm.yyyy'
Например 03.01.2009, если пользователь ответил неверно, то выводим правильный ответ,
но уже в следующем виде: третье января 2009 года, склонением можно пренебречь
В конце считаем количество правильных и неправильных ответов и предлагаем начать снова
"""
import random
birthdays_dict = {'Уинстона Черчилля':'30.11.1874',
                  'Махатмы Ганди':'02.10.1869',
                  'Микельанджело':'06.03.1475',
                  'Виктора Пелевина':'22.11.1962',
                  'Юрия Дудя':'11.10.1986',
                  'Ивана Грозного':'25.08.1530',
                  'Сергея Рахманинова':'20.03.1873',
                  'Михаила Лермонтова':'15.10.1814',
                  'Михаила Булгакова':'15.05.1891',
                  'Михаила Врубеля':'17.03.1856',
                  'Юрия Гагарина':'09.03.1934',
                  'Софьи Ковалевской':'15.01.1850'
                  }
month_dict = {'01':'января',
              '02':'февраля',
              '03':'марта',
              '04':'апреля',
              '05':'мая',
              '06':'июня',
              '07':'июля',
              '08':'августа',
              '09':'сентября',
              '10':'октября',
              '11':'ноября',
              '12':'декабря'}
days_dict = {'30':'тридцатого',
             '02':'второго',
             '06':'шестого',
             '22':'двадцать второго',
             '11':'одиннадцатого',
             '25':'двадцать пятого',
             '20':'двадцатого',
             '15':'пятнадцатого',
             '09':'девятого',
             '17':'семнадцатого'
}

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
result = random.sample(numbers, 5)
key_list = list(birthdays_dict.keys())
toRepeat = True
while toRepeat:
    correct_answer_num = 0
    for i in result:
        #str_qest
        answer = input("Введите дату рождения " + key_list[i] + ': ')
        correct_answer_str = birthdays_dict.get(key_list[i])
        correct_answer = correct_answer_str.split('.')
        if answer == correct_answer_str:
            correct_answer_num += 1
        else:
            print('Неверно. Правильный ответ - {0} {1} {2} года'.format(days_dict.get(correct_answer[0]), month_dict.get(correct_answer[1]), correct_answer[2]))

    correct_answer_proc = correct_answer_num/5
    print('Ваш результат:')
    print('\tПравильных ответов:\t', correct_answer_num)
    print('\tНеправильных ответов:', 5 - correct_answer_num)
    print('\tПроцент правильных ответов {:5.1%}'.format(correct_answer_proc))
    print('\tПроцент неправильных ответов {:5.1%}'.format(1 - correct_answer_proc))
    answer = input("Хотите начать игру заново (y/n): ")
    if answer != 'y':
        toRepeat = False