'''  Користувачем вводиться початковий і кінцевий рік. Створити цикл, який виведе всі високосні роки в цьому проміжку (границі включно). P.S. Рік є високосним, якщо він кратний 4, але не кратний 100, а також якщо він кратний 400. '''

try:
    first_year = int(input('Enter first year: '))
    last_year = int(input('Enter last year: '))

    for i in range(first_year, last_year):
        if i %4 == 0 and i % 100 != 0:
            print(i)
        elif i % 400 == 0:
            print(i)

except ValueError:
    print(f'Enter the year as a number.\nFor example: 2000')
