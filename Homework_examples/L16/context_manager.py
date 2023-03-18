"""
Написать класс Timer для измерения времени выполнения кода.
Прошедшее время должен возвращать в аттрибуте elapsed_time.
Класс должен применяться как контекстный менеджер.
У класса должен быть метод reset.
Если между использованием контекстного менеджера вызывался метод reset, прошедшее время должно считаться заново.
Если метод reset не вызывался, в elapsed_time должно быть сохранено время выполнения всех фрагментов кода обернутых контекстным менеджером.
class Timer:
    pass


Пример использования:
with Timer() as t:
    time.sleep(1)
print(t.elapsed_time)  # ~1 second
with t:
    time.sleep(2)  # ~3 seconds
print(t.elapsed_time)

with Timer() as t2:
    time.sleep(1)
print(t2.elapsed_time)  # ~1 second
t2.reset()
with t2:
    time.sleep(2)  # ~2 seconds
print(t2.elapsed_time)

"""


import time


class Timer:

    def __init__(self):
        self.reset()

    def __enter__(self):
        self.start_time = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.perf_counter()
        self.elapsed_time_accumulator += self.end_time - self.start_time

    @property
    def elapsed_time(self):
        return self.elapsed_time_accumulator

    def reset(self):
        self.elapsed_time_accumulator = 0


if __name__ == '__main__':
    with Timer() as t:
        time.sleep(1)
    print(t.elapsed_time)  # ~1 second

    time.sleep(2)

    with t:
        time.sleep(2)  # ~3 seconds
    print(t.elapsed_time)

    with Timer() as t2:
        time.sleep(1)
    print(t2.elapsed_time)  # ~1 second

    t2.reset()
    time.sleep(1)

    with t2:
        time.sleep(2)  # ~2 seconds
    print(t2.elapsed_time)
