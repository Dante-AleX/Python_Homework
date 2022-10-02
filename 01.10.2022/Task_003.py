# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу 
# между максимальным и минимальным значением дробной части элементов.

from random import uniform, randrange

my_list = [round(uniform(0, value), 2) for value in range(1, randrange(10,20))]
new_list = [round(val%1, 2) for val in my_list if isinstance(val, float)]

print(new_list)
print(max(new_list) - min(new_list))
