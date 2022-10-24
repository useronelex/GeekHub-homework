'''Створіть функцію для валідації пари ім'я/пароль за наступними правилами:
   - ім'я повинно бути не меншим за 3 символа і не більшим за 50;
   - пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну
   цифру;
   - якесь власне додаткове правило :)
   Якщо якийсь із параметрів не відповідає вимогам - породити виключення із відповідним текстом.
'''

class LenNameExeption(Exception):
    pass

class LenPasswordException(Exception):
    pass

class IsAlphaPasswordException(Exception):
    pass

class TitleNameException(Exception):
    pass


def valid_data(name, password):
    try:
        if len(name) > 50  or len(name) < 3:
            raise LenNameExeption('Out of range lenght name')
        elif len(password) < 8:
            raise LenPasswordException('short password')
        elif password.isalpha():
            raise IsAlphaPasswordException('password dos\'t have latter')
        elif not name.istitle():
            raise TitleNameException('name must be Upper')
        else:
            return 'Ok!'
    except LenNameExeption as error:
        return error
    except LenPasswordException as error:
        return error
    except IsAlphaPasswordException as error:
        return error
    except TitleNameException as error:
        return error
    except Exception as error:
        return error

      
try:
    print(valid_data('Jerry', '1hnb5678'))
except(ValueError, NameError, TypeError) as err:
    print(f'You have error: {err}')
