''' Написати функцiю season, яка приймає один аргумент (номер мiсяця вiд 1 до 12) та яка буде повертати пору року, до якої цей мiсяць належить (зима, весна, лiто або осiнь). У випадку некоректного введеного значення - виводити відповідне повідомлення. '''

def season(month):
    try:
        if month <= 0 or month > 12:
            print('The month value must be in the range 0 to 12')
        else:
            if month <= 2 or month == 12:
                print('winter')
            elif 2 < month <= 5:
                print('spring')
            elif 5 < month <= 8:
                print('summer')
            else:
                print('autumn')
    except TypeError:
        print('Wrong data type entered.\nPleace, enter number from 0 to 12.')                 
         
                
season(12)    
