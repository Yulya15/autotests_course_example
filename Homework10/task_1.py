# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

import random
import string


def generate_random_name():
    """
    Генератор двух слов
    :return: два слова из латинских букв от 1 до 15 символов, разделенных пробелами
    """
    while True:
        string_1 = ''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(1, 15)))
        string_2 = ''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(1, 15)))
        yield f'{string_1} {string_2}'


gen = generate_random_name()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
