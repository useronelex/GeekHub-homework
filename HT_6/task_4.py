''' Створіть функцію <morse_code>, яка приймає на вхід рядок у вигляді коду Морзе та виводить декодоване значення (латинськими літерами).
   Особливості:
    - використовуються лише крапки, тире і пробіли (.- )
    - один пробіл означає нову літеру
    - три пробіли означають нове слово
    - результат може бути case-insensitive (на ваш розсуд - великими чи маленькими літерами).
    - для простоти реалізації - цифри, знаки пунктуацїї, дужки, лапки тощо використовуватися не будуть. Лише латинські літери.
    - додайте можливість декодування сервісного сигналу SOS (...---...)
    Приклад:
    --. . . -.- .... ..-- -...   .. ...   .... . .-. .
    результат: GEEKHUB IS HERE '''


import re

def morse_code(message):
    if not message.isalpha():
        code_message = []
        words = re.split('   +', message)

        for word in words:
            for latter in word.split():
                for key, value in morse.items():
                    if latter == value:
                        code_message.append(key)
            code_message.append(' ')      
        print(*code_message, sep='')       
    elif message.isalpha():
        word = message.upper().strip()
        code_message = []

        for latter in word:
            for key, value in morse.items():
                    if latter == key:
                        code_message.append(value)
            code_message.append(' ')
        print(*code_message, sep='')
    else:
        print('You enter something wrong')
    

morse = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
         'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
         'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..--', 'V': '...-', 'W': '.--', 'X': '-..-',
         'Y': '-.--', 'Z': '--..', ' ': ' '
        }
s = '--. . . -.- .... ..-- -...   .. ...   .... . .-. .'
sos = 'sos'

try:
    morse_code(s)
except (ValueError, NameError, TypeError):
    print('Incorrect data')