''' Написати функцію, яка буде реалізувати логіку циклічного зсуву елементів в списку. Тобто функція приймає два аргументи: список і величину зсуву (якщо ця величина додатна - пересуваємо з кінця на початок, якщо від'ємна - навпаки - пересуваємо елементи з початку списку в його кінець).
   Наприклад:
   fnc([1, 2, 3, 4, 5], shift=1) --> [5, 1, 2, 3, 4]
   fnc([1, 2, 3, 4, 5], shift=-2) --> [3, 4, 5, 1, 2] '''


def shift(ls_numbers, step):
    if step > 0:
        for i in range(step):
            ls_numbers.insert(0, ls_numbers.pop())
        return ls_numbers
    else:
        for i in range(abs(step)):
            ls_numbers.append(ls_numbers.pop(0))
        return ls_numbers


try:   
    print(shift([1, 2, 3, 4, 5], -2))
except (ValueError, NameError, TypeError) as err_log:
    print(f'Have a problem: {err_log}')
