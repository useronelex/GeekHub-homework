''' Write a script which accepts a decimal number from user and converts it to hexadecimal. '''

number = int(input('Enter your decimal number: '), 10)
hex_number = hex(number)

print(f'Your hexadecimal number: {hex_number}')
