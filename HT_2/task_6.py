''' Write a script to check whether a value from user input is contained in a group of values.
    e.g. [1, 2, 'u', 'a', 4, True] --> 2 --> True
         [1, 2, 'u', 'a', 4, True] --> 5 --> False '''


def foo(ls, s):
    for value in ls:
        lis = str(value)
        if s == lis:
            return True
    return False

ls = [1, 2, 'u', 'a', 4, True]
s = input()


print(foo(ls, s))
