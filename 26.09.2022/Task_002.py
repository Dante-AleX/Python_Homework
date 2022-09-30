# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# 5=1*2*3*4*5

n = int(input('Please insert a whole positive number: '))
fact = 1

if n < 1:
    print('Invalid number')

for i in range (1, n+1):
    fact = fact*i
print(f'The factorial of {n} is: {fact}')