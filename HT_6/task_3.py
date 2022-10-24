'''На основі попередньої функції (скопіюйте кусок коду) створити наступний скрипт:
   а) створити список із парами ім'я/пароль різноманітних видів (орієнтуйтесь по правилам своєї функції) - як валідні, так і ні;
   б) створити цикл, який пройдеться по цьому циклу і, користуючись валідатором, перевірить ці дані і надрукує для кожної пари значень відповідне повідомлення, наприклад:
      Name: vasya
      Password: wasd
      Status: password must have at least one digit
      -----
      Name: vasya
      Password: vasyapupkin2000
      Status: OK
   P.S. Не забудьте використати блок try/except ;)
'''

class LenNameExeption(Exception):
    pass

class LenPasswordException(Exception):
    pass

class IsAlphaPasswordException(Exception):
    pass

class TitleNameException(Exception):
    pass


def check_status(l):
    name = 0
    password = 1

    for i in l:
        try:
            if len(i[name]) > 50  or len(i[name]) < 3:
                raise LenNameExeption('Out of range lenght name')
            elif len(i[password]) < 8:
                raise LenPasswordException('short password')
            elif i[password].isalpha():
                raise IsAlphaPasswordException('password dos\'t have latter')
            elif not i[name].istitle():
                raise TitleNameException('name must be Upper')
            else:
                status = 'Ok!'
        except LenNameExeption:
            status = 'Out of range lenght name'
        except LenPasswordException:
            status = 'short password'
        except IsAlphaPasswordException:
            status = 'password dos\'t have latter'
        except TitleNameException:
            status = 'name must be Upper'
        except Exception:
            status = 'Unspecified'

        print(f'Name: {i[name]}\nPassword: {i[password]}\nStatus: {status}\n-------')


l = [('Bill', '1234567k'), ('Tomy', 'qnbw213'), ('Li', 'dsffhbb32'), ('volly', 'nmjhg32234n'), ]
try:
    check_status(l)
except (NameError, ValueError, TypeError) as err:
    print('You have a problem: {err}')
