import time
import threading

data = threading.local()
"""класс local позволяет создавать и хранить данные внутри потока. Данные закрыты для других потоков"""

def get():
    print(data.value)


def t1():
    data.value = 555
    get()


def t2():
    data.value = 222
    get()


threading.Thread(target=t1).start()
threading.Thread(target=t2).start()
