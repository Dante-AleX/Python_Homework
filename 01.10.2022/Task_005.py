# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

num = 8
my_list = [1, 0, 1]
for _ in range(1, num):
    print(my_list[0], my_list[1] - my_list[0] )
    print(my_list[-1], my_list[-2] + my_list[-1])
    my_list.append(my_list[-2] + my_list[-1])
    my_list.insert(0, my_list[1] - my_list[0])


# def input_numbers ():
#     while True :
#         numb = input('Insert a number: ')
#         try:
#             numbers = int(numb)
#             return numbers
#         except:
#             print('Not a number')

# def get_two_numb (num):
#     numb_1 = 1
#     numb_2 = 1
#     fibo_nums = []
#     for i in range(num):
#         fibo_nums.append(numb_1)
#         numb_1, numb_2 = numb_2, numb_1 + numb_2
#     numb_1 = 0
#     numb_2 = 1
#     for i in range(num+1):
#         fibo_nums.insert(0, numb_1)
#         numb_1, numb_2 = numb_2, numb_1 - numb_2
#     return fibo_nums


# number = input_numbers()
# print(f'Nega Fibonacci - {get_two_numb(number)}')
