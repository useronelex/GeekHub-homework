''' Write a script which accepts a <number>(int) from user and generates dictionary in range <number> where key is <number> and value is <number>*<number>
    e.g. 3 --> {0: 0, 1: 1, 2: 4, 3: 9} '''

number = int(input('Enter integer number: '))
list_numers = []
i = 0

while i < number:
   list_numers.append(i)
   i += 1
dictionary = {el: el*el for el in list_numers}

print(dictionary)
