''' Користувач вводить змінні "x" та "y" з довільними цифровими значеннями. Створіть просту умовну конструкцію (звiсно вона повинна бути в тiлi ф-цiї), під час виконання якої буде перевірятися рівність змінних "x" та "y" та у випадку нерівності - виводити ще і різницю.
    Повинні працювати такі умови (x, y, z заміність на відповідні числа):
    x > y;       вiдповiдь - "х бiльше нiж у на z"
    x < y;       вiдповiдь - "у бiльше нiж х на z"
    x == y.      відповідь - "х дорівнює y" '''


def equales_numbs(x, y):
    if x == y:
        return f'{x} дорівнює {y}'
    elif x > y:
        z = x -y
        return f'{x} більше нiж {y} на {z}'
    else:
        z = y - x
        return f'{y} більше нiж {x} на {z}' 


try:
    x = int(input('Enter x: '))
    y = int(input('Enter y: '))
    
    print(equales_numbs(x, y))
except ValueError:
    print('A decimal integer was expected')
