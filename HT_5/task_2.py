''' Написати функцію <bank> , яка працює за наступною логікою: користувач робить вклад у розмірі <a> одиниць строком на <years> років під <percents> відсотків (кожен рік сума вкладу збільшується на цей відсоток, ці гроші додаються до суми вкладу і в наступному році на них також нараховуються відсотки). Параметр <percents> є необов'язковим і має значення по замовчуванню <10> (10%). Функція повинна принтануть суму, яка буде на рахунку, а також її повернути (але округлену до копійок). '''

def bank(a, years, percent= 10):
    sum_percent_a = 0
    p = percent / 100
    for i in range(years):
        sum_percent_a = a * p
        a += sum_percent_a  
    return round(a)

try:    
    print(bank(100, 2, 10))
except (ValueError, TypeError):
    print('Invalid value')
