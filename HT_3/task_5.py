''' Write a script to remove values duplicates from dictionary. Feel free to hardcode your dictionary. '''

dict = {'foo': 'bar', 
        'bar': 'buz',
        'foo': 'bar', 
        'bar': 'buz',
        'ttt': '145'
        }
new_dict = {}

for key,value in dict.items():
    if value not in new_dict.values():
        new_dict[key] = value

print(new_dict)
