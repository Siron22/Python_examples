import random
from threading import Thread, current_thread, Barrier
import time


def foo(barrier):
    slp = random.randint(3, 7)
    time.sleep(slp)
    print(f"Поток [{current_thread().name}] запущен в {time.ctime()}")
    barrier.wait()
    print(f"Поток [{current_thread().name}] преодолел барьер")


bar = Barrier(3)
"""
Класс Barrier(3) принимает количество потоков и тормозит и ждёт пока каждый не дойдёт до метода .wait(), 
после этого все потоки одновременно переходят к выполнению дальнейшего кода.
*** количество запускаемых потоков должно быть кратно количеству потоков которые принимает барьер,
выполнение кода будет продолжено только по достижению метода .wait() заданным количеством потоков!!!!
"""

for i in range(15):
    Thread(target=foo, args=(bar,), name=f"thr-{i}").start()
