from multiprocessing import Process, RLock, current_process
import time

"""
Класс RLock (Reentrant Lock) в multiprocessing является аналогом класса RLock из модуля threading, 
но предназначен для использования в многопроцессорных приложениях. Основное отличие между Lock и RLock 
заключается в том, что RLock может быть захвачен несколько раз одним и тем же процессом, но должен 
быть освобожден столько же раз, прежде чем другие процессы смогут получить доступ к критической секции кода.

Основные отличия:

    Повторное захватывание: RLock позволяет процессу многократно захватывать блокировку, что означает, что 
    процесс может многократно вызывать метод acquire() без вызова release(), при условии, что это выполняется 
    в рамках одного процесса. В то время как обычный Lock такое поведение не поддерживает и может привести 
    к блокировке (deadlock).
    Усложненное поведение: RLock более сложный по сравнению с обычным Lock, поскольку он должен отслеживать 
    количество захватов и освобождений, чтобы гарантировать корректное поведение при множественных захватах 
    и освобождениях.
    
*** Может быть освобожден только процессом, который заблокировал
"""

def worker_with_rlock(lock):
    lock.acquire()
    try:
        print(f"Процесс {current_process().name} начал выполнение с RLock")
        lock.acquire()  # Многократное захватывание
        try:
            print(f"Процесс {current_process().name} продолжил выполнение с RLock")
            time.sleep(2)
            print(f"Процесс {current_process().name} завершил выполнение с RLock")
        finally:
            lock.release()
    finally:
        lock.release()


if __name__ == "__main__":

    rlock = RLock()
    processes = []

    for _ in range(2):
        p = Process(target=worker_with_rlock, args=(rlock, ))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()
