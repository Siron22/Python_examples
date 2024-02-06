import time
import threading

value = 0
locker = threading.Lock()
"""
Lock() блокирует область кода для остальных процессов, пока активный процесс не завершит работу
!!!! c помощью метода Lock().release() другой поток может разблокировать закрытую область кода
"""

# locker = threading.RLock()
"""
При использовании RLock разблокировать доступ к коу может ТОЛЬКО ТОТ процесс который его заблокировал
"""


# def inc_value():
#     global value
#     while True:
#         locker.acquire()
#         value += 1
#         print(value)
#         time.sleep(0.1)
#         locker.release()

def inc_value():
    global value
    while True:
        with locker:  # Locker() поддерживает работу с контекстным менеджером
            value += 1
            print(value)
            time.sleep(0.1)


"""!!!! c помощью метода locker.release() другой поток может разблокировать закрытую область кода"""

for i in range(5):
    threading.Thread(target=inc_value).start()
