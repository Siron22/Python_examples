import time
import threading


def timer_test():
    while True:
        print("test")
        time.sleep(1.15)


the = threading.Timer(5, timer_test)
the.daemon = True
the.start()
"""класс Timer() задаёт время через запуститься процесс, при этом не блокирует выполнение основного кода.
Наследуется от Tread(), а также имеет собственный метод .cancel(), который может отменить выполнение 
потока ДО его запуска"""

# while True:
#     print('11111')
#     time.sleep(1)

for _ in range(3):
    print('11111')
    time.sleep(1)

the.cancel()
print("finish")
