import time
import multiprocessing


def func():
    for _ in range(3):
        print(f"{multiprocessing.current_process().name} - {time.ctime()}")
        time.sleep(1)


# pr = multiprocessing.Process(target=func, name="prc-1")
# pr.start()
# print("Process started")
# print("Process is alive: ", pr.is_alive())
# print("PID: ", pr.pid)
# print("Deamon: ", pr.daemon) # parameter can be changed only before start

# pr.kill()
# pr.terminate()

prc = []

for i in range(3):
    pr = multiprocessing.Process(target=func, name=f"prc-{i}")
    pr.start()
    print(f"PID [prc-{i}]: ", pr.pid)
    prc.append(pr)

for i in prc:
    i.join()  # wait until all processes finished

print("All processes are terminated")
