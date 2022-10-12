'''  Користувачем вводиться початковий і кінцевий рік. Створити цикл, який виведе всі високосні роки в цьому проміжку (границі включно). P.S. Рік є високосним, якщо він кратний 4, але не кратний 100, а також якщо він кратний 400. '''

try:
   first_year = int(input('Enter first year: '))
   last_year = int(input('Enter last year: '))
   while first_year <= last_year:
      if first_year %4 == 0 and first_year % 100 != 0:
         print(first_year)
      elif first_year % 400 == 0:
         print(first_year)
      first_year += 1
   else:
      print('First entered year has more value then value last entered  year')
except ValueError:
   print(f'Enter the year as a number.\nFor example: 2000')
