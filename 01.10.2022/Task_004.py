# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

from tokenize import Octnumber


def int_input(message):
    str1 = input(message)
    if str1.isdigit():
        result = int(str1)
    else:
        print('Введено не число')
        result = -1
    return result


res_dec = int_input('Введите число: ')
print(f'{res_dec} => {bin(res_dec)[2:]}')
