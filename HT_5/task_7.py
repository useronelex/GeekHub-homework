''' Написати функцію, яка приймає на вхід список (через кому), підраховує кількість однакових елементів у ньому і виводить результат. Елементами списку можуть бути дані будь-яких типів.
    Наприклад:
    1, 1, 'foo', [1, 2], True, 'foo', 1, [1, 2] ----> "1 -> 3, foo -> 2, [1, 2] -> 2, True -> 1" '''


def counting_elements(lst):
    lst_key = [i for i in range(len(lst))]
    dict_lst = dict(zip(lst_key, lst))
    l = []
    for i in lst:
        if i not in l:
            count = 0
            for k, v in dict_lst.items():
                if i == v:
                    count += 1
            print(f'{i} -> {count}')
            l.append(i)


lst = [4, 3, 'foo', [1, 2], True, 'foo', 3, [1, 2]]
counting_elements(lst)
