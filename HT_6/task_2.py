'''Створіть функцію для валідації пари ім'я/пароль за наступними правилами:
   - ім'я повинно бути не меншим за 3 символа і не більшим за 50;
   - пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну
   цифру;
   - якесь власне додаткове правило :)
   Якщо якийсь із параметрів не відповідає вимогам - породити виключення із відповідним текстом.
'''

class InvalidException(Exception):
    ...


def valid_data(name, password):

    if 3 < len(name) < 50 and len(password) >= 8 and not password.isdigit() and name.istitle():
        print('Your data is correctly!')
    else:
        raise InvalidException('Some Error')


valid_data('Jerry', '1h345678')