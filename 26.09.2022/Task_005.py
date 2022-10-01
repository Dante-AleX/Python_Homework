# Реализуйте алгоритм перемешивания списка.

from random import randint

list = [1, 2, 3, 4, 5, 6]
for index_i in range(len(list)):
    index_j = randint(0, len(list) - 1)
    help = list[index_i]
    list[index_i] = list[index_j]
    list[index_j] = help
print(list)
