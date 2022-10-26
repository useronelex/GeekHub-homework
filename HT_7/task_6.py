''' Напишіть функцію,яка приймає рядок з декількох слів і повертає довжину найкоротшого слова. 
    Реалізуйте обчислення за допомогою генератора в один рядок. '''


def short_word(string):
    return f'Довжина найкоротшого слова: {min([len(i) for i in string.split()])}'


string = 'GEEKHUB IS HERE'

try:
    print(short_word(string))
except (ValueError, AttributeError, TypeError, NameError) as err:
    print(f'Error: {err}')