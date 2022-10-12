''' Створити цикл від 0 до ... (вводиться користувачем). В циклі створити умову, яка буде виводити поточне значення, якщо остача від ділення на 17 дорівнює 0. '''

try:
   number = int(input('Введіть число: '))
   counter = 0
   while counter < number:
      counter += 1
      if counter % 17 == 0:
         print(counter)
except ValueError as err:
   print(f'Enter corect value. {err} is not integer number.') 
