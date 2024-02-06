import random
import time
from threading import Thread, Event, current_thread, active_count

event = Event()
"""
Класс Event в модуле threading предоставляет механизм для синхронизации потоков, 
позволяя одному потоку сообщать другим о наступлении определенных событий.
Поток блокируется на его ожидании с помощью метода wait(), а затем основной поток 
устанавливает событие, вызывая метод set(), что позволяет заблокированному потоку продолжить выполнение.
"""

event.clear()  # Event False


def image_handler():
    thr_num = current_thread().name
    print(f"Идет подготовка изображения из потока [{thr_num}]")
    event.wait()


for i in range(10):
    print(f"Поток {i} запущен")
    Thread(target=image_handler, name=str(i)).start()
    time.sleep(1)

if active_count() >= 10:
    event.set()  # Event True
