# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

import random

num = int(input("Введите натуральную степень k: "))


def magit_to_file(num: int):
    if num > 0:
        num1 = random.randint(0,100)   
        str_1 = f"{num1}*x^{num}"
        for i in reversed(range(1, num)):
            num1 = random.randint(0,100)    
            if num1 != 0:
                str_1 += f" + {num1}*x^{i}"
        num1 = random.randint(0,100)
        if num1 != 0:
            print(f"{str_1} + {num1} = 0")
        else:
            print(f"{str_1} = 0")

magit_to_file(num)
