''' Write a script that will run through a list of tuples and replace the last value for each tuple. The list of tuples can be hardcoded. The "replacement" value is entered by user. The number of elements in the tuples must be different. '''

value = input('Enter somethin: ')
tuple_list = [(1, 2, 3), (4, 5, 6, 6.5, 6.75), (7, 8, 9,10), ()]
new_tuple_list = []

if all(tuple_list):
    for elem_list in tuple_list:
        ls_tuple_elements = list(elem_list)
        ls_tuple_elements.pop()
        ls_tuple_elements.append(value)
        elem_list = tuple(ls_tuple_elements)
        new_tuple_list.append(elem_list)
    print(new_tuple_list)    
else:
    print('You have empty tuple')
