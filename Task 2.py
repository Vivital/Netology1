"""
Задание 2
Дана переменная, в которой хранится число (год).
Необходимо написать программу, которая выведет,
является ли данный год високосным или обычным.
"""
year = 2021

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print('Високосный год')
else:
    print('Обычный год')