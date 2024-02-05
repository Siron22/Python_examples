import time
import threading

# параметр deamon означает, что запущенный поток прекратит работу сразу после окончания работы основного
# потока приложения
def get_data(data):
    while True:
        print(f"[{threading.current_thread().name}] - {data}")
        time.sleep(1)


thr = threading.Thread(target=get_data, args=(str(time.time()),), daemon=True)
thr.daemon = False # альтернативный способ назначения атрибутаLockr
thr.start()

time.sleep(3)
print('Finish')


