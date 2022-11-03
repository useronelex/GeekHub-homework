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


def light_trafic(colors_car, colors_human):
    for cl_car in colors_car:
        for cl_hm in colors_human:
            for i in range(4):
                if  cl_car != cl_hm and cl_car != 'Yellow':
                    print(f'{cl_car}   {cl_hm}')
                    time.sleep(1)
            if cl_car == 'Yellow':
                print('Yellow   Red')
                time.sleep(1)
    
    

if __name__ == '__main__':
    colors_car = ['Red', 'Yellow', 'Green']
    colors_human = ['Red', 'Green']
    
    light_trafic(colors_car, colors_human)
