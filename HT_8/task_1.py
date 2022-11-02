'''       Програма-світлофор.
    Створити програму-емулятор світлофора для авто і пішоходів. Після запуска програми на екран виводиться 
    в лівій половині - колір автомобільного, а в правій - пішохідного світлофора. Кожну 1 секунду виводиться поточні кольори. 
    Через декілька ітерацій - відбувається зміна кольорів - логіка така сама як і в звичайних світлофорах 
    (пішоходам зелений тільки коли автомобілям червоний).
    Приблизний результат роботи наступний:
        Red        Green
        Red        Green
        Red        Green
        Red        Green
        Yellow     Red
        Yellow     Red
        Green      Red
        Green      Red
        Green      Red
        Green      Red
        Yellow     Red
        Yellow     Red
        Red        Green
'''

import time


def light_trafic():
    colors_for_car = ['Red', 'Yellow', 'Green']
    colors_for_human = ['Red', 'Green']
    
    for color in colors_for_car:
        for i in range(3):
            for cl_car in colors_for_car:
                for cl_human in colors_for_human:
                    if color == cl_car and cl_car != cl_human and cl_car != 'Yellow':
                        print(f'{cl_car}        {cl_human}')
                        time.sleep(1)
                    elif color == cl_car and cl_car == 'Yellow':
                        print(f'{cl_car}        Red')
                        time.sleep(1)


if __name__ == '__main__':
    light_trafic()