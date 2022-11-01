import csv


def start():
    """ The function responsible for the main functionality of the program """

    def user_check(login, password):
        """ The function checks for the correctness of user data input """
        try:
            with open('users/users.csv', 'r', encoding='utf-8', newline='') as users_file:
                users_data = csv.DictReader(users_file)
                for row in users_data:
                    if row['login'] == login and row['password'] == password:
                        print(f"Вітаємо, {row['first_name']} {row['last_name']}\nВи ввійшли до системи!\n======================")
                        return True
                    else:
                        print('Дані не знайдено')
                    #     try:
                    #         choice = int(input('-> '))
                    #     except (ValueError, TypeError, NameError):
                    #         print('Невірний формат введення')
                    #         return user_check()
                    #     if choice == 1:
                    #         check_balance(user_first_name, user_second_name)
                    #     elif choice == 2:
                    #         put_money(user_first_name, user_second_name)
                    #     elif choice == 0:
                    #         return print("Bye!")
                    # elif  user_login != login and user_password != password:
                    #     print('Ви ввели не вірні дані.\nСпробуйте ще раз\n======================')
                    #     return user_check()
        except FileNotFoundError:
            with open('users/users.csv', 'w', encoding='utf-8', newline='') as users_file:
                header = ['first_name', 'last_name', 'login', 'password']
                users_data = csv.DictWriter(users_file, fieldnames=header)
                users_data.writeheader()
                first_name = input()
                last_name = input()
                login = input()
                password = input()
                users_data.writerow({'first_name':first_name, 'last_name': last_name, 'login': login, 'password': password})

    def check_balance(first_name, second_name):
        """ A function that checks the user's balance """
        try:
            with open(f'users_balance/{first_name}_{second_name}_balance.txt', 'r', encoding='utf-8') as user_balance:
                balance = user_balance.read()
                print(f'На вашому рахунку {balance} UAH')
        except FileNotFoundError:
            with open(f'users_balance/{first_name}_{second_name}_balance.txt', 'w', encoding='utf-8') as user_balance:
                user_balance.write(0)

    def put_money(first_name, second_name):
        """ Function of depositing funds by the user to the account """
        with open(f'users_balance/{first_name}_{second_name}_balance.txt', 'r+', encoding='utf-8') as user_balance:
            try:
                deposit_money = int(input('Введіть суму: '))
                if deposit_money != 0:
                    x = user_balance.read()
                    print(x)
                    # balance = x + deposit_money
                    # print(balance)
                    # print(type(balance))
                    # user_balance.write(str())
                    # print(f'Ви поклали {new_balance} UAH')
                else:
                    print('Ви нічого не поклали!')
            except (TypeError, ValueError) as e:
                print(f'Не вірний формат введення! {e}')

    first_name = input('Введіть ім\'я: ')
    second_name = input('Введіть прізвище : ')
    login = input('Введіть логін: ')
    password = input('Введіть пароль: ')

    # Start menu
    menu = 'Select an operation: \n' \
           '1. Перевірити рахунок\n' \
           '2. Покласти кошти\n' \
           '3. Зняти кошти\n' \
           '0. Вихід'

    if user_check(login, password):
        print(menu)
        choice = int(input('-> ').strip())
        if choice == 1:
            check_balance(first_name, second_name)
        elif choice == 2:
            put_money(first_name, second_name)

    else:
        return user_check()



if __name__ == '__main__':
    start()
