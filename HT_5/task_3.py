''' Написати функцию <is_prime>, яка прийматиме 1 аргумент - число від 0 до 1000, и яка вертатиме True, якщо це число просте і False - якщо ні. '''

import math

def is_prime(number):
    if 0 <= number <= 1000:
        if number < 2:
            return False
        else:
            for i in range(2, int(math.sqrt(number)) + 1):
                if number % i == 0:
                    return False
            return True
    else:
        return 'Out of range'

        
try:
    print(is_prime(4))
except (TypeError, NameError) as log_err:
    print(f'You have a problem: {log_err}')
