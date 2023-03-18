"""
Написать декоратор skip, которым можно декорировать функции.
Если переданное выражение condition истинное, функция не должна выполнятся, а должно вывестись строка reason.
Если выражение condition ложное, функция должна выполнится.

def skip(condition, reason=''):
   pass

Пример использования:
@skip(condition=True, reason='Skipped because of JIRA-123 bug')
def test_two_plus_two():
   assert 2 + 2 == 5

test_two_plus_two()  # Skipped because of JIRA-123 bug
"""


def skip(condition, reason):
    def skip_inner(func):
        if condition:
            print(reason)

            def wrapper(*args, **kwargs):
                pass
        else:
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)
        return wrapper
    return skip_inner


@skip(condition=True, reason='Skipped because of JIRA-123 bug')
def test_two_plus_two():
    assert 2 + 2 == 5


test_two_plus_two()  # Skipped because of JIRA-123 bug
