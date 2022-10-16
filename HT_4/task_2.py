''' Створіть 3 рiзних функцiї (на ваш вибiр). Кожна з цих функцiй повинна повертати якийсь результат (напр. інпут від юзера, результат математичної операції тощо). Також створiть четверту ф-цiю, яка всередині викликає 3 попередні, обробляє їх результат та також повертає результат своєї роботи. Таким чином ми будемо викликати одну (четверту) функцiю, а вона в своєму тiлi - ще 3. '''


def get_name():
    name = input('Enter name: ')
    return name


def sum_numbers(x, y):
    return x + y


def cats_names(*names):
    return names


def data_list(x, y, *names):
    return [get_name(), sum_numbers(x, y), cats_names(*names)]


print(data_list(2, 3, 'Tom', 'Jery', 'Sir Thomas'))
