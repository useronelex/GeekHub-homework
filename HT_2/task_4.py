''' Write a script which accepts a <number> from user and then <number> times asks user for string input. At the end script must print out result of concatenating all <number> strings. '''

number = int(input('Enter your number: '))
count = 0
string = str()

while (count < number):
    count += 1
    words = input ('Enter your words: ')
    string = string + words
    
print(string)
    


