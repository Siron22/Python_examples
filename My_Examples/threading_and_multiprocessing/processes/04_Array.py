from multiprocessing import Process, Array, current_process
import time

"""
Класс Array из модуля multiprocessing представляет собой разделяемый между процессами массив, 
который можно использовать для обмена данными между процессами. Этот массив может быть использован 
для хранения данных одного типа, такого как целые числа, числа с плавающей запятой и т. д.
"""


def increment_counter(counter):
    for _ in range(5):
        for i in range(len(counter)):
            counter[i] += 1
    print(f"[{current_process().name}] - {list(counter)}")

if __name__ == "__main__":
    # Создаем разделяемый между процессами массив целых чисел размером 3
    shared_counter = Array('i', [0, 0, 0])

    # Выводим начальное состояние счетчика
    print("Начальное состояние счетчика:", shared_counter[:])

    # Создаем и запускаем два процесса
    processes = []
    for _ in range(5):
        p = Process(target=increment_counter, args=(shared_counter,))
        p.start()
        processes.append(p)

    # Ждем завершения всех процессов
    for p in processes:
        p.join()

    # Выводим конечное состояние счетчика
    print("Конечное состояние счетчика:", shared_counter[:])
