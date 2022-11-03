""" 
Програма-банкомат.
   Використовуючи функції створити програму з наступним функціоналом:
      - підтримка 3-4 користувачів, які валідуються парою ім'я/пароль (файл <users.CSV>);
      - кожен з користувачів має свій поточний баланс (файл <{username}_balance.TXT>) та історію транзакцій (файл <{username_transactions.JSON>);
      - є можливість як вносити гроші, так і знімати їх. Обов'язкова перевірка введених даних (введено цифри; знімається не більше, ніж є на рахунку і т.д.).
   Особливості реалізації:
      - файл з балансом - оновлюється кожен раз при зміні балансу (містить просто цифру з балансом);
      - файл - транзакціями - кожна транзакція у вигляді JSON рядка додається в кінець файла;
      - файл з користувачами: тільки читається. Але якщо захочете реалізувати функціонал додавання нового користувача - не стримуйте себе :)
   Особливості функціонала:
      - за кожен функціонал відповідає окрема функція;
      - основна функція - <start()> - буде в собі містити весь workflow банкомата:
      - на початку роботи - логін користувача (програма запитує ім'я/пароль). Якщо вони неправильні - вивести повідомлення про це і закінчити роботу (хочете - зробіть 3 спроби, а потім вже закінчити роботу - все на ентузіазмі :))
      - потім - елементарне меню типн:
        Введіть дію:
           1. Подивитись баланс
           2. Поповнити баланс
           3. Вихід
      - далі - фантазія і креатив, можете розширювати функціонал, але основне завдання має бути повністю реалізоване :)
    P.S. Увага! Файли мають бути саме вказаних форматів (csv, txt, json відповідно)
    P.S.S. Добре продумайте структуру програми та функцій
"""

import csv
import json


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
            raise Exception('Перевищено кількість спроб!')
    except FileNotFoundError:
        raise Exception('Створіть файл users.csv')


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

    flag = True
    while flag:
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
                flag = False


if __name__ == '__main__':
    start()
