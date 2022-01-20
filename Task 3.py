"""
Задание 3
Необходимо написать программу, которая будет запрашивать у пользователя
месяц и дату рождения и выводить соответствующий знак зодиака.
"""
day = int(input('Введите день: '))
month = input('Введите месяц: ')

if (31 >= day >= 20 and month == 'Январь') or 19 >= day >= 1 and month == 'Февраль':
    print('Ваш знак зодиака: Водолей')
elif (29 >= day >= 20 and month == 'Февраль') or 20 >= day >= 1 and month == 'Март':
    print('Ваш знак зодиака: Рыбы')
elif (31 >= day >= 21 and month == 'Март') or 20 >= day >= 1 and month == 'Апрель':
    print('Ваш знак зодиака: Овен')
elif (30 >= day >= 21 and month == 'Апрель') or 20 >= day >= 1 and month == 'Май':
    print('Ваш знак зодиака: Телец')
elif (31 >= day >= 21 and month == 'Май') or 20 >= day >= 1 and month == 'Июнь':
    print('Ваш знак зодиака: Близнецы')
elif (30 >= day >= 21 and month == 'Июнь') or 22 >= day >= 1 and month == 'Июль':
    print('Ваш знак зодиака: Рак')
elif (31 >= day >= 23 and month == 'Июль') or 22 >= day >= 1 and month == 'Август':
    print('Ваш знак зодиака: Лев')
elif (30 >= day >= 23 and month == 'Август') or 22 >= day >= 1 and month == 'Сентябрь':
    print('Ваш знак зодиака: Дева')
elif (31 >= day >= 23 and month == 'Сентябрь') or 22 >= day >= 1 and month == 'Октябрь':
    print('Ваш знак зодиака: Весы')
elif (30 >= day >= 23 and month == 'Октябрь') or 22 >= day >= 1 and month == 'Ноябрь':
    print('Ваш знак зодиака: Скорпион')
elif (30 >= day >= 23 and month == 'Ноябрь') or 21 >= day >= 1 and month == 'Декабрь':
    print('Ваш знак зодиака: Стрелец')
elif (31 >= day >= 22 and month == 'Декабрь') or 19 >= day >= 1 and month == 'Январь':
    print('Ваш знак зодиака: Козерог')
else:
    print('Неверный ввод')