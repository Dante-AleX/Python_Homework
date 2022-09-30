# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка 
# (или на какой оси она находится).

x = int(input('Please, insert an X coordinate: '))
y = int(input('Please, insert an Y coordinate: '))

if x>0 and y> 0:
    print('This coordinates belong to the first quarter')
elif x<0 and y>0:
    print('This coordinates belong to the second quarter')
elif x<0 and y<0:
    print('This coordinates belong to the third quarter')
elif x>0 and y<0:
    print('This coordinates belong to the forth quarter')
elif x==0 and y==0:
    print('These are invalid coordinates')