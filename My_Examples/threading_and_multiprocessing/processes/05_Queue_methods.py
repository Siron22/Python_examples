import random
from multiprocessing import Process, Queue


def get_text(q):
    val = random.randint(1, 10)
    q.put(str(val))


queue = Queue(maxsize=11)
print("<<<<<<< Before >>>>>>>>>>")
print(f"qsize(): {queue.qsize()}")
print(f"empty(): {queue.empty()}")
print(f"full(): {queue.full()}")
print()

pr_list = []

for _ in range(10):
    pr = Process(target=get_text, args=(queue,))
    pr_list.append(pr)
    pr.start()

for pr in pr_list:
    pr.join()

# Помещаем специальный флаг в конце очереди
queue.put(None)

print("<<<<<<< After >>>>>>>>>>")
print(f"qsize(): {queue.qsize()}")
print(f"empty(): {queue.empty()}")
print(f"full(): {queue.full()}")
print()

print("<<<<<<< Elements >>>>>>>>>>")
while True:
    item = queue.get()
    if item is None:
        break
    print(item)
