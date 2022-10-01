# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

n = int(input('Insert a number: '))
my_list = [[n, round(((1+1/n)**n),2)] for n in range(1,n+1)]
print('Sequence of numbers: ', dict(my_list))
print('The sum of the sequence: ', sum(dict(my_list)))
