import threading
import time


# def get_data(data):
#     while True:
#         print(f"[{threading.current_thread().name}] - {data}")
#         time.sleep(2)
#
#
# thr = threading.Thread(target=get_data, args=(str(time.time()),))
# thr.start()
#
# print("name: ", threading.main_thread().name)
# threading.main_thread().name = "New_Name" # set new name for thread after initializing
# print("result: ", threading.main_thread().name)


# for i in range(100):
#     print(f"current: {i}")
#     time.sleep(1)
#
#     if i % 5 == 0:
#         print('active thread: ', threading.active_count()) # quantity of active threads
#         print('enumerate: ', threading.enumerate()) # list of all active threads
#         print('thr-1 is alive: ', thr.is_alive()) # bool - is this thread alive


# # join() - этот метод запускает потоки, ожидает их окончания и только после этого переходит к следующему коду
def get_data(data, value):
    for _ in range(value):
        print(f"[{threading.current_thread().name}] - {data}")
        time.sleep(1)


thr_list = []

for i in range(10):
    thr = threading.Thread(target=get_data, args=(str(time.time()), i), name=f"thr-{i}")
    thr_list.append(thr)
    thr.start()

print(thr_list)

for i in thr_list:
    i.join()


print('Finish')

