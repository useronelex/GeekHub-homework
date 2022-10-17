''' Наприклад маємо рядок --> "f98neroi4nr0c3n30irn03ien3c0rfe kdno400we(nw,kowe%00koi!jn35pijnp4 6ij7k5j78p3kj546p4 65jnpoj35po6j345" -> просто потицяв по клавi =)
   Створіть ф-цiю, яка буде отримувати довільні рядки на зразок цього та яка обробляє наступні випадки:
    -  якщо довжина рядка в діапазоні 30-50 (включно) -> прiнтує довжину рядка, кiлькiсть букв та цифр
    -  якщо довжина менше 30 -> прiнтує суму всіх чисел та окремо рядок без цифр та знаків лише з буквами (без пробілів)
    -  якщо довжина більше 50 -> щось вигадайте самі, проявіть фантазію =) '''


def get_string(string):
    alpha_string = ''.join((i for i in string if i.isalpha()))
    num_string = ''.join((i for i in string if i.isdigit()))
    if len(string) == 0:
        print('Порожній рядок') 
    elif 30 <= len(string) <= 50:
        print (f'Довжина рядка: {len(string)} символи.\nРядок містить {len(alpha_string)} літер та {len(num_string)} цифр')
    elif len(string) < 30:
        sum_num_string = sum(int(n) for n in num_string)
        print(f'Сума чисел = {sum_num_string}.\nРядок літер - {alpha_string}')    
    else:
        user_sub_string = input('Введіть шукані символи - ')
        try:
            find_sub_string = string.index(user_sub_string)
            print(f'Шукані символи знайдено у {find_sub_string} позиції рядку')
        except ValueError:
            print('Шукані символи в рядку не знайдено!')

     
# long, middle, short, empty  -  strings for tests        
long = '98neroi4nr0c3n30irn03ien3c0rfe kdno400we(nw,kowe%00koi!jn35pijnp4 6ij7k5j78p3kj546p4 65jnpoj35po6j345'
middle = '98neroi4nr0c3n39irn03ien3crghghfe'
short = '6ij7  k5j78'
empty = ''

try:
    get_string(middle)
except(TypeError, SyntaxError, NameError) as err: 
    print(f'Виникла помилка! {err}')
