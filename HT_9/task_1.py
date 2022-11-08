"""
Банкомат 2.0
    - усі дані зберігаються тільки в sqlite3 базі даних у відповідних таблицях. Більше ніяких файлів. Якщо в попередньому завданні ви добре продумали структуру програми то у вас не виникне проблем швидко адаптувати її до нових вимог.
    - на старті додати можливість залогінитися або створити нового користувача (при створенні нового користувача, перевіряється відповідність логіну і паролю мінімальним вимогам. Для перевірки створіть окремі функції)
    - в таблиці з користувачами також має бути створений унікальний користувач-інкасатор, який матиме розширені можливості (домовимось, що логін/пароль будуть admin/admin щоб нам було простіше перевіряти)
    - банкомат має власний баланс
    - кількість купюр в банкоматі обмежена (тобто має зберігатися номінал та кількість). Номінали купюр - 10, 20, 50, 100, 200, 500, 1000
    - змінювати вручну кількість купюр або подивитися їх залишок в банкоматі може лише інкасатор
    - користувач через банкомат може покласти на рахунок лише суму кратну мінімальному номіналу що підтримує банкомат. В іншому випадку - повернути "здачу" (наприклад при поклажі 1005 --> повернути 5). Але це не має впливати на баланс/кількість купюр банкомату, лише збільшується баланс користувача (моделюємо наявність двох незалежних касет в банкоматі - одна на прийом, інша на видачу)
    - зняти можна лише в межах власного балансу, але не більше ніж є всього в банкоматі.
    - при неможливості виконання якоїсь операції - вивести повідомлення з причиною (невірний логін/пароль, недостатньо коштів на рахунку, неможливо видати суму наявними купюрами тощо.)
    - файл бази даних з усіма створеними таблицями і даними також додайте в репозиторій, що б ми могли його використати
"""


import sqlite3
import json


def reg_user():
    """ Registration new user """
    login = input('Login: ').strip()
    password = input('Password: ').strip()
    with sqlite3.connect('base.db') as con:
        c = con.cursor()
        c.execute("INSERT INTO users(login, password, balance, is_incasator) VALUES (?, ?, ?, ?)", (login, password, 0, False))
        con.commit()


def user_check(user_login, password):
    """ The function checks for the correctness of user data input """
    with sqlite3.connect("base.db") as db:
        c = db.cursor()
        user_data = c.execute("SELECT login, password FROM users").fetchall()
        if (user_login, password) in user_data:
            return True


def check_balance(user_login):
    """ A function that checks the user's balance """
    with sqlite3.connect("base.db") as db:
        c = db.cursor()
        balance = c.execute("SELECT balance FROM users WHERE login = :login", {'login': user_login}).fetchone()[0]
        print(f'На вашому рахунку {balance} UAH')
        return balance


def user_transaction(user_login, **kwarks):
    """ Function containing user transactions """
    data = {
        'active': kwarks['active'],
        'balance': kwarks['balance'],
        'amount': kwarks['amount']
    }
    data = json.dumps(data)
    with sqlite3.connect('base.db') as conn:
        c = conn.cursor()
        c.execute("INSERT INTO trans_log (name, active) VALUES (?,?)", (user_login, data))
        conn.commit()


def put_money(user_login):
    """ Function of depositing funds by the user to the account """
    balance = check_balance(user_login)
    deposit_money = abs(int(input('Введіть суму: ')))
    new_balance = balance + deposit_money

    with sqlite3.connect("base.db") as con:
        c = con.cursor()
        c.execute("UPDATE users SET balance = ? WHERE login = ?", (new_balance, user_login))
        con.commit()

    user_transaction(user_login, active='Deposit', balance=new_balance, amount=deposit_money)


def withdraw_money(user_login):
    """ Function of depositing funds by the user to the account """
    balance = check_balance(user_login)
    amount_money = abs(int(input('Введіть суму: ')))
    new_balance = balance - amount_money
    total_atm_balance = atm_check_total() - amount_money
    if new_balance <= 0 or total_atm_balance <= 0:
        print('Недостатньо коштів для зяняття')
    else:
        with sqlite3.connect("base.db") as con:
            c = con.cursor()
            c.execute("UPDATE users SET balance = ? WHERE login = ?", (new_balance, user_login))
            con.commit()
        user_transaction(user_login, active='Withdrawal', balance=new_balance, amount=-amount_money)


def atm_check_total():
    """ The function checks the total amount of ATM funds """
    with sqlite3.connect("base.db") as con:
        cur = con.cursor()
        total = cur.execute("SELECT * FROM atm_finance").fetchall()
        atm_balance = []
        for record in total:
            atm_balance.append(record[0] * record[1])
        return sum(atm_balance)


def view_atm_balance(admin_login):
    """ Viewing the ATM balance by the administrator """
    print(f"Баланс банкомата: {atm_check_total()} UAH")



# FUNCTIONS TO START
def start_registration_user():
    """" A function that works in the main function for registering new users """
    user_menu = '===================\n' \
                'Select an operation: \n' \
                '1. Перевірити рахунок\n' \
                '2. Покласти кошти\n' \
                '3. Зняти кошти\n' \
                '0. Вихід'
    reg_user()
    with sqlite3.connect("base.db") as con:
        c = con.cursor()
        login = c.execute("SELECT max(ROWID), login FROM users").fetchone()[1]
        flag = True
        while flag:
            print(user_menu)
            choice = int(input('-> ').strip())
            if choice == 1:
                check_balance(login)
            elif choice == 2:
                put_money(login)
            elif choice == 3:
                withdraw_money(login)
            elif choice == 0:
                print('Bye!')
                flag = False


def start_users_verification(login, password):
    """ A function that works in the main function to check for an existing user or administrator """
    user_menu = '===================\n' \
                'Select an operation: \n' \
                '1. Перевірити рахунок\n' \
                '2. Покласти кошти\n' \
                '3. Зняти кошти\n' \
                '0. Вихід'
    admin_menu = '===================\n' \
                 'Select an operation: \n' \
                 '1. Баланс банкомата\n' \
                 '0. Вихід'
    flag = True
    while flag:
        if user_check(login, password):
            # USER CHECK
            with sqlite3.connect("base.db") as con:
                c = con.cursor()
                user = c.execute("SELECT is_incasator FROM users WHERE login = :login", {'login': login}).fetchone()[0]
                if not user:
                    print(user_menu)
                    choice = int(input('-> ').strip())
                    if choice == 1:
                        check_balance(login)
                    elif choice == 2:
                        put_money(login)
                    elif choice == 3:
                        withdraw_money(login)
                    elif choice == 0:
                        print('Bye!')
                        flag = False
                # ADMIN CHECK
                else:
                    print(admin_menu)
                    choice = int(input('-> ').strip())
                    if choice == 1:
                        view_atm_balance(login)
                    elif choice == 0:
                        print('Bye!')
                        flag = False
        # RETRIES LOGIN
        else:
            print('======================')
            print('Не вірно введені дані!\nСпробуйте ще раз!')
            print('======================')
            attempt = 3
            count = 0
            while count < attempt:
                login = input('Введіть логін: ').strip()
                password = input('Введіть пароль: ').strip()
                if user_check(login, password):
                    break
                count += 1
                count_user = attempt - count
                print('======================')
                print(f'Не вірно введені дані!\nСпробуйте ще раз! Кількість спроб: {count_user}')
                print('======================')
            else:
                print('Ви перевищили кількість спроб!\nBye!')
                flag = False


def start():
    """ The function responsible for the main functionality of the program """
    start_menu = '===================\n' \
                 'Select an operation: \n' \
                 '1. Новий користувач\n' \
                 '2. Маю облікові дані'

    print(f"WELCOME!\n{start_menu}")
    choice = int(input('-> ').strip())
    # REGISTER NEW USER
    if choice == 1:
        start_registration_user()
    elif choice == 2:
        login = input('Введіть логін: ').strip()
        password = input('Введіть пароль: ').strip()
        start_users_verification(login, password)


if __name__ == '__main__':
    start()
