"""
Написать функцию, которая возвращает слуайную строку заданной длины.
Строка должна состоять из больших и маленьких латинских букв и цифр.

def get_random_string(length: int) -> str:
    pass

Ограничения:
- Не использовать модуль string
- Не создавать руками список ['a', 'b', 'c', ..., 'X', 'Y', 'Z', 0, 1, ..., 8, 9]

Write function that returns random string consisting only small and capital letters of specified length:
def get_random_string(length: int) -> str
Restrictions:
- Don't use module string
- Don't create manually list ['a', 'b', 'c', ..., 'X', 'Y', 'Z', 0, 1, ..., 8, 9]
"""
import random


def get_random_string(length: int) -> str:
    code_0 = 48  # 0
    code_9 = 57  # 57
    code_capital_a_ = 65  # A
    code_capital_z = 90  # Z
    code_small_a = 97  # a
    code_small_z = 122  # z
    char_codes = list(range(code_0, code_9 + 1)) + list(range(code_capital_a_, code_capital_z + 1)) + list(range(code_small_a, code_small_z + 1))
    return ''.join([chr(random.choice(char_codes)) for _ in range(length)])


for i in [1, 2, 6, 10, 99]:
    print(get_random_string(i))
