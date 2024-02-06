import random
import time
from threading import Thread, BoundedSemaphore, current_thread, active_count

max_conn = 5

pool = BoundedSemaphore(value=max_conn)
"""
класс BoundedSemaphore позволяет регулировать количество потоков, которые имеют доступ к области кода.
даёт доступ новому потоку только когда появилось свободное место.
Для блокир/разблокирования применяются методы .acquire() и .release() либо контекстный менеджер with
"""


def semaphor():
    while True:
        with pool:
            slp = random.randint(1, 5)
            time.sleep(slp)
            print(f"{current_thread().name} - sleep {slp}")
            print('active: ', active_count())
            print('*' * 50)


for i in range(10):
    Thread(target=semaphor).start()
