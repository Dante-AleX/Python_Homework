# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

def Sum(n):

    sum = 0
    while (n != 0):

        sum = sum + (n % 10)
        n = n//10

    return sum


n = int(input('Please insert a real number: '))
if n==0:
    print('Invalid number')
print(Sum(n))
