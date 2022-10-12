''' Write a script to remove empty elements from a list.
    Test list: [(), ('hey'), ('',), ('ma', 'ke', 'my'), [''], {}, ['d', 'a', 'y'], '', []] '''


list_elements = [(), ('hey'), ('',), ('ma', 'ke', 'my'), [''], {}, ['d', 'a', 'y'], '', []]

new_list = list(filter(None, list_elements))

print(new_list)
