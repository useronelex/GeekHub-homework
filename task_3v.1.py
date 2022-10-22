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

class LenNameException(Exception):
    pass

class LenPasswordException(Exception):
    pass

class TitleNameException(Exception):
    pass

class AlphaPasswordException(Exception):
    pass


def valid_data():

    l = [('Vasya', '1234567j'), ('Vahhhh', '1234568887')] 
    status = ''    

    for i in l:
        name = 0
        password = 1
        try:
            if 3 < len(i[name]) < 50 and len(i[password]) >= 8 and not i[password].isdigit() and i[name].istitle():
                status =  'Ok' 
                print('---------')  
            else:
                if  3 < len(i[name]) < 50:
                    raise LenNameException('invalid number of characters') 
                elif len(i[password]) >= 8:
                    raise LenPasswordException('short password')
                elif i[name].istitle():
                    raise TitleNameException('The name is not title')
                elif not i[password].isdigit():
                    raise AlphaPasswordException('password does not contain letters')

        except LenNameException:
            status = 'The name mast be more then 3 characters'
            print('---------') 
        except LenPasswordException:
            status = 'password must contain more than 8 values'
            print('---------') 
        except TitleNameException:
            status = 'The Name is not Title'
            print('---------') 
        except AlphaPasswordException:
            status = 'password does not contain letters'
            print('---------') 
        

        print(f'Name: {i[name]}\nPassword: {i[password]}\nStatus: {status}')
        name += 1
        password += 1


valid_data()