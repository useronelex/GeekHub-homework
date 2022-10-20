''' Написати функцію <fibonacci>, яка приймає один аргумент і виводить всі числа Фібоначчі, що не перевищують його. '''

def fibonacci(x):
    sum_x = 0
    for i in range(x + 1):
        if sum_x < x:
            sum_x += i
            print(sum_x)  

try:        
    fibonacci(6)
except(TypeError, NameError, ValueError) as err_log:
    print(f'You have a problem: {err_log}')


