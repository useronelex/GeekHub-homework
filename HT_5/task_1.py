'''  Написати функцію <square>, яка прийматиме один аргумент - сторону квадрата, і вертатиме 3 значення у вигляді кортежа: периметр квадрата, площа квадрата та його діагональ. '''

import math


def square(a):
    perim_square = 4*a
    area_square = a**2
    diagonal_square = a*math.sqrt(2)
    return (perim_square, area_square, diagonal_square)


try:
    print(square(6))
except (TypeError, NameError) as err: 
    print(f'You haw a problem: {err}')
