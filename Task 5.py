"""
Задание 5
Дана переменная, в которой хранится шестизначное число (номер проездного билета).
Напишите программу, которая будет определять, является ли данный билет "счастливым".
Билет считается счастливым, если сумма первых трех цифр совпадает с суммой последних трех цифр номера.
"""
number = 351243
s = [int(i) for i in str(number)]
sum1 = sum(s[0:3])
print(f'Сумма первых трёх чисел: {sum1}')
sum2 = sum(s[3::])
print(f'Сумма последних трёх чисел: {sum2}')
if sum1 == sum2:
    print('Счастливый билет')
else:
    print('Несчастливый билет')