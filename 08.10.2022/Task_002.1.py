# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

from random import randint


def input_dat(name):
    x = int(
        input(f"{name}, insert the number of candies you'll take from 1 to 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, insert a correct number: "))
    return x


def p_print(name, k, counter, value):
    print(
        f"{name}, took {k} candies, now he/she has {counter}. {value} candies left.")


player1 = input("First player, insert your name: ")
player2 = input("Second player, insert your name: ")
value = int(input("Insert the number of candies on the table: "))
flag = randint(0, 2)  # флаг очередности
if flag:
    print(f"{player1} goes first")
else:
    print(f"{player2} goes first")

counter1 = 0
counter2 = 0

while value > 28:
    if flag:
        k = input_dat(player1)
        counter1 += k
        value -= k
        flag = False
        p_print(player1, k, counter1, value)
    else:
        k = input_dat(player2)
        counter2 += k
        value -= k
        flag = True
        p_print(player2, k, counter2, value)

if flag:
    print(f"{player1} won")
else:
    print(f"{player2} won")
