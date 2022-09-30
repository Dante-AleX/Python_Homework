# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

x = int(input('Please, insert the number of the quarter of the axis: '))

if x == 1:
    print('The range of possible coordinates is X = [0;+∞), Y = [0;+∞)')
elif x == 2:
    print('The range of possible coordinates is X = (-∞;0], Y = [0;+∞)')
elif x == 3:
    print('The range of possible coordinates is X = (-∞;0], Y = (-∞;0]')
elif x == 4:
    print('The range of possible coordinates is X = [0;+∞), Y = (-∞;0]')
else:
    print('Invalid number')
