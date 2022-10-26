''' Напишіть функцію, яка приймає 2 списки. Результатом має бути новий список, 
    в якому знаходяться елементи першого списку, яких немає в другому. Порядок елементів, 
    що залишилися має відповідати порядку в першому (оригінальному) списку. Реалізуйте обчислення за допомогою генератора в один рядок.
    Приклад:
    array_diff([1, 2], [1]) --> [2]
    array_diff([1, 2, 2, 2, 3, 4], [2]) --> [1, 3, 4] '''


def array_diff(list_1, list_2):
    return [elem for elem in list_1 if not elem in list_2]


try:
    print(array_diff([1, 2], [1]))
    print(array_diff([1, 2, 2, 2, 3, 4], [2]))
except (ValueError, AttributeError, TypeError, NameError) as err:
    print(f'Error: {err}')
