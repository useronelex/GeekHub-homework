''' Написати функцію <fibonacci>, яка приймає один аргумент і виводить всі числа Фібоначчі, що не перевищують його. '''

def fibonacci(x):
    n1 = 0
    n2 = 1
    while n2 < x:
        print(n2, end=' ')
        n1, n2 = n2, n1 + n2

try:        
    fibonacci(100)
except(TypeError, NameError, ValueError) as err_log:
    print(f'You have a problem: {err_log}')
