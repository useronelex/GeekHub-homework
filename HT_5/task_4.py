''' Написати функцію <prime_list>, яка прийматиме 2 аргументи - початок і кінець діапазона, і вертатиме список простих чисел всередині цього діапазона. Не забудьте про перевірку на валідність введених даних та у випадку невідповідності - виведіть повідомлення. '''

import math

def is_prime(start_num, stop_num): 
    list_num = []
    
    for num in range(start_num, stop_num + 1):
        if all(num %i != 0 for i in range(2, int(math.sqrt(num)) + 1)): 
            if num > 1:
                list_num.append(num)
                
    print(list_num)

   
try:
    is_prime(0, 21)
except (TypeError, NameError, ValueError) as log_err:
    print(f'You have a problem: {log_err}')
