# Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.

x = int(input('Please insert a number that corresponds to a day of the week: '))

if x == 6 or x == 7:
    print('This is a weekend day')
elif x >= 1 and x <= 5:
    print('This is a work day')
else:
    print('Invalid number')
