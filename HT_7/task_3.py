'''Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї функції. Тобто щоб її можна було використати у вигляді:
    for i in my_range(1, 10, 2):
        print(i)
    1
    3
    5
    7
    9
    
    P.S. Повинен вертатись генератор.
    P.P.S. Для повного розуміння цієї функції - можна почитати документацію по ній: https://docs.python.org/3/library/stdtypes.html#range
    P.P.P.S Не забудьте обробляти невалідні ситуації (типу range(1, -10, 5) тощо). Подивіться як веде себе стандартний range в таких випадках.'''


def my_range(start, stop, step= 1):
    l = []
    while True:
        if start < stop and step > 0:
            l.append(start)
            start += step
        elif abs(start) < stop and step < 0:
            l.append(start)
            start += step
        elif start < stop and step < 0 or start == stop:
            yield l
            break
        else:
            break
    for i in l:
        yield i
      
    
try:
    for i in my_range(1, 10, 2):
        print(i)
except (ValueError, NameError, TypeError) as error:
    print(f'Error: {error}')



