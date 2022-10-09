''' Write a script to concatenate all elements in a list into a string and print it. List must include both strings and integers and must be hardcoded. '''

ls = [1, 'i', 4, 'october']
new_elem = str()

for elem in ls:
    elem = str(elem)
    new_elem += elem
    
print (new_elem)
