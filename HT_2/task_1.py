''' Write a script which accepts a sequence of comma-separated 
    numbers from user and generates a list and a tuple with 
    those numbers.'''

numbers = input()
list_numbers = numbers.split(',')
tuple_numbers = tuple(numbers.split(','))

print(list_numbers)
print(tuple_numbers)
