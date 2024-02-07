import multiprocessing
import random
from multiprocessing import Process, Array, current_process, Lock
import time


def add_value(locker, array, index):
    with locker:
        num = random.randint(1, 100)
        sl = random.randint(1, 4)
        vtime = time.ctime()
        array[index] = num
        print(f"prc: {current_process().name}, array[{index}]: {num}, time: {vtime}")
        time.sleep(sl)


if __name__ == "__main__":
    lock = Lock()
    arr = Array("i", range(10))

    # Создаем и запускаем несколько процессов
    processes = []
    for i in range(10):
        p = Process(target=add_value, args=(lock, arr, i))
        p.start()
        processes.append(p)

    # Ждем завершения всех процессов
    for p in processes:
        p.join()

    # Выводим результаты
    print("Результаты инкрементации:", list(arr))
