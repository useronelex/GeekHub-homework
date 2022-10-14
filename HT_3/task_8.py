''' Створити цикл від 0 до ... (вводиться користувачем). В циклі створити умову, яка буде виводити поточне значення, якщо остача від ділення на 17 дорівнює 0. '''

try:
    number = int(input('Введіть число: '))
    for i in range(number):
        if i % 17 == 0:
            print(i)

except ValueError as err:
    print(f'Enter corect value. {err} is not integer number.') 
