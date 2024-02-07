from multiprocessing import Process, Lock, current_process
import time

"""
В библиотеке multiprocessing класс Lock() предоставляет механизм блокировки для синхронизации доступа к общему 
ресурсу между процессами. Это аналог класса Lock из модуля threading, но предназначенный для использования в 
многопроцессорных приложениях.

Описание работы:
    Lock используется для блокировки ресурса на время выполнения критической секции кода, гарантируя, что только 
    один процесс имеет доступ к этому ресурсу в любой момент времени.
    Подобно threading.Lock, он имеет методы acquire() и release(), которые позволяют захватывать и освобождать 
    блокировку соответственно.
    При использовании Lock в multiprocessing каждый процесс имеет свой собственный экземпляр блокировки.

*** может быть освобожден другим процессом
"""


# Функция, которую будет выполнять процесс
def worker(lock):
    lock.acquire()
    try:
        print(f"Процесс {current_process().name} начал выполнение")
        time.sleep(1)
        print(f"Процесс {current_process().name} завершил выполнение")
    finally:
        lock.release()


if __name__ == "__main__":
    # Создание объекта Lock
    lock = Lock()

    # Создание и запуск процессов
    processes = []
    for _ in range(5):
        p = Process(target=worker, args=(lock, ))
        p.start()
        processes.append(p)

    # Ожидание завершения работы процессов
    for p in processes:
        p.join()
