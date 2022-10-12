''' Write a script to get the maximum and minimum VALUE in a dictionary. '''

dict = {'foo': '1', 
        'bar': '2',
        'baz': '3'
        }

min_key = min(dict, key = dict.get)
max_key = max(dict, key = dict.get)

print(f'Min value in dictionary: {dict.get(min_key)}\nMax value in dictionary: {dict.get(max_key)}')
