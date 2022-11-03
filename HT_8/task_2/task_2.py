'''Написати функцію, яка приймає два параметри: ім'я (шлях) файлу та кількість символів. Файл також додайте в репозиторій.
        На екран має бути виведений список із трьома блоками - символи з початку, 
                                                                із середини 
                                                                та з кінця файлу. 
        Кількість символів в блоках - та, яка введена в другому параметрі. 
        Придумайте самі, як обробляти помилку, наприклад, коли кількість символів більша, ніж є в файлі або, 
    наприклад, файл із двох символів і треба вивести по одному символу, то що виводити на місці середнього блоку символів?). 
    Не забудьте додати перевірку чи файл існує.
'''


def file_processing(name, size):
    try:
        if name == 'test.txt':
            with open(name, 'r', encoding='utf-8') as file:
                if size <= len(file.read()):
                    # start position
                    file.seek(0)
                    f_1 = file.read(size)
                    # center position
                    file.seek(round((len(file.read()) / 2)))
                    f_2 = file.read(size)
                    # end position
                    file.seek(file.seek(0) + len(file.read()) - size)
                    f_3 = file.read(size)
                    print(f'{f_1},  {f_2},  {f_3}')
                else:
                    print('the number of characters is greater than in the file')
        else:
            raise FileNotFoundError('file not found')
    except FileNotFoundError as err:
        print(f'Error: {err}')


if __name__ == '__main__':
    try:
        n = abs(int(input('Value symbols: ')))
        file_processing('test.txt', n)
    except (ValueError, NameError, TypeError) as error:
        print(f'incorrectly entered data: {error}')
