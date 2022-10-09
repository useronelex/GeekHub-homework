''' Write a script which accepts a <number> from user and print out 
	a sum of the first <number> positive integers.'''


number = int(input('Enter your number: '))
s = 0

for i in range(number+1):
    s += i  
  
print(f'Sum the first positive integers are {s}')
