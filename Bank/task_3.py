import csv
import json


class EnterException(Exception):
    pass

#-------------Створюю нового користувача --------
def create_user():
    print('Потрібна реєстрація!\n================')
    with open('users/users.csv', 'w', encoding='utf-8', newline='') as file:
        first_name = input('Ваше ім\'я: ')
        last_name = input('Ваше прізвище: ')
        login = input('Login: ')
        password = input('Password: ')

        fieldnames = ['first_name', 'last_name', 'login', 'password']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'first_name': first_name, 'last_name': last_name, 'login': login, 'password': password})


def user_check(user_login, password):
    """ The function checks for the correctness of user data input """
    try:
        with open('users/users.csv', 'r', encoding='utf-8', newline='') as users_file:
            users_data = csv.DictReader(users_file)
            for row in users_data:
                if row['login'] == user_login and row['password'] == password:
                    return True
            print('Дані не знайдено')
            for attempt in range(3):
                if row['login'] == user_login and row['password'] == password:
                    return True
                else:
                    login = input('Введіть логін: ').strip()
                    password = input('Введіть пароль: ').strip()
                    count = 2
                    count -= attempt
                    print(f'Невірно введені дані, спробуйте ще\nКількість спроб - {count}')
            raise EnterException('Перевищено кількість спроб!')
    except FileNotFoundError:
        create_user()            # --------------------> не створює новий файл, а відпрацьовує user_check()
    except EnterException as err:
        return err                 #  -------------> хочу обробити красиво падіння, тоді теж саме, працює далі функція user_check()


def check_balance(user_login):
    """ A function that checks the user's balance """
    try:
        with open(f'users_balance/{user_login}_balance.txt', 'r', encoding='utf-8') as user_balance:
            balance = user_balance.read()
            print(f'На вашому рахунку {balance} UAH')
            return balance
    except FileNotFoundError:
        with open(f'users_balance/{user_login}_balance.txt', 'w', encoding='utf-8') as user_balance:
            user_balance.write('0')
            print(f'На вашому рахунку 0 UAH')
            return '0'


def put_money(user_login):
    """ Function of depositing funds by the user to the account """
    balance = check_balance(user_login)
    deposit_money = abs(int(input('Введіть суму: ')))
    new_balance = int(balance) + deposit_money
    with open(f'users_balance/{user_login}_balance.txt', 'w', encoding='utf-8') as user_balance:
        user_balance.write(str(new_balance))
        user_transaction(user_login, active='deposit', balance=new_balance, amount=deposit_money)
        print(f'Ваш рахунок поповнено на {deposit_money} UAH\nВаш баланс {new_balance} UAH')


def user_transaction(user_login, **kwarks):
    data = {
        'active': kwarks['active'],
        'balance': kwarks['balance'],
        'amount': kwarks['amount']
    }
    try:
        with open(f'users_transactions/{user_login}_transaction.json', 'r', encoding='utf-8') as file:
            file_data = json.load(file)
            file_data.append(data)
        with open(f'users_transactions/{user_login}_transaction.json', 'w', encoding='utf-8') as file:
            json.dump(file_data, file, indent=4)
    except FileNotFoundError:
        with open(f'users_transactions/{user_login}_transaction.json', 'w', encoding='utf-8') as file:
            json.dump([data], file, indent=4)


def start():
    """ The function responsible for the main functionality of the program """
    login = input('Введіть логін: ').strip()
    password = input('Введіть пароль: ').strip()
    print('======================')
    if user_check(login, password):
        print(f"Вітаємо, Ви ввійшли до системи!\n======================")

    start = True
    while start:
        # Start menu
        menu = 'Select an operation: \n' \
               '1. Перевірити рахунок\n' \
               '2. Покласти кошти\n' \
               '0. Вихід'

        if user_check(login, password):
            print(menu)
            choice = int(input('-> ').strip())
            if choice == 1:
                check_balance(login)
            elif choice == 2:
                put_money(login)
            elif choice == 0:
                print('Bye!')
                start = False


if __name__ == '__main__':
    start()
