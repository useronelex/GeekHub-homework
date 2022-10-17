''' Write a script that will run through a list of tuples and replace the last value for each tuple. The list of tuples can be hardcoded. The "replacement" value is entered by user. The number of elements in the tuples must be different. '''

value = input('Enter some values: ')
tuple_list = [(1, 2, 3), (), (4, 5, 6, 6.5, 6.75), (7, 8, 9,10), ()]
new_tuple_list = []

for element_list in tuple_list:
    if element_list:
        new_tuple_list += [element_list[:-1] + (value,)]  
    else: 
        new_tuple_list += (element_list, )

print(new_tuple_list)
