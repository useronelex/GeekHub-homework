''' Ну і традиційно - калькулятор. Повинна бути 1 функцiя, яка приймає 3 аргументи - один з яких операцiя, яку зробити! 
    Аргументи брати від юзера (можна по одному - окремо 2, окремо +, окремо 2; можна всі разом - типу 2 + 2). 
    Операції що мають бути присутні: +, -, *, /, %, //, **. Не забудьте протестувати з різними значеннями на предмет помилок! '''


def calculator(num_1, num_2, operation):
    if operation == '':
        print('Ви не вказали операцію')
    elif operation == '+':
        addition(num_1, num_2)
    elif operation == '-':
        subtraction(num_1, num_2)
    elif operation == '*':
        multiplication (num_1, num_2)
    elif operation == '/':
        division (num_1, num_2)
    elif operation == '%':
        modulus (num_1, num_2)
    elif operation == '**':
        exponentiation (num_1, num_2)
    elif operation == '//':
        floor_division (num_1, num_2)
    else:
        print('Невідома операція')


def addition(num_1, num_2):
    rezult = num_1 + num_2
    print(f'{num_1} + {num_2 } = {rezult}')
    
 
def subtraction(num_1, num_2):
    rezult = num_1 - num_2
    print(f'{num_1} - {num_2 } = {rezult}')


def multiplication(num_1, num_2):
    rezult = num_1 * num_2
    print(f'{num_1} * {num_2 } = {rezult}')
        

def division(num_1, num_2):
    if num_2 != 0:
        rezult = num_1 / num_2
        print(f'{num_1} / {num_2 } = {rezult}')
    else:
        print('Ділення на 0!')
    
    
def modulus(num_1, num_2):
    if num_2 != 0:
        rezult = num_1 % num_2
        print(f'{num_1} % {num_2 } = {rezult}')
    else:
        print('Ділення на 0!')   
    

def exponentiation(num_1, num_2):
    rezult = num_1 ** num_2
    print(f'{num_1} ** {num_2 } = {rezult}') 


def floor_division(num_1, num_2):
    if num_2 != 0:
        rezult = num_1 // num_2
        print(f'{num_1} // {num_2 } = {rezult}')
    else:
        print('Ділення на 0!')
        
        
try:    
    num_1 = float(input('Введіть перше число: '))
    num_2 = float(input('Введіть друге число: '))
    operation = input('Вкажіть математичну операцію:').strip()

    calculator(num_1, num_2, operation)
except ValueError:
    print('Невірний формат даних')
