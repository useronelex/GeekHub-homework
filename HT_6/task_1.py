''' 1. Створіть функцію, всередині якої будуть записано СПИСОК із п'яти користувачів (ім'я та пароль). 
    Функція повинна приймати три аргументи: два - обов'язкових (<username> та <password>) і третій - необов'язковий параметр 
    <silent> (значення за замовчуванням - <False>).
    Логіка наступна:
        якщо введено правильну пару ім'я/пароль - вертається True;
        якщо введено неправильну пару ім'я/пароль:
            якщо silent == True - функція повертає False
            якщо silent == False - породжується виключення LoginException (його також треба створити =))
'''
class LoginException(Exception):
    pass


def check_function(username, password, silent= False):
    l = [('Tom', 123), ('Bary', 32344), ('Clay', 5432), ('Calvin', 65432), ('John', 3241)]

    if (username, password) in l:
        return True
    else:
        if silent:
            return False
        else:
            raise LoginException('masssage error')
          

print(check_function('Tom', 1233, True))
