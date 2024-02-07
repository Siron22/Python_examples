import multiprocessing


def get_value(value):
    name = multiprocessing.current_process().name
    print(f"[{name}] - {value}")
    return value


def end_func(response):
    print("All is done ", response)
"""
эта функция необходима для сбора результатов выполнения основной функции всех процессов.
Аргумент response передаётся в неё автоматически и может быть далее использован в коде
"""

if __name__ == "__main__":
    with multiprocessing.Pool(processes=8) as p:
        p.map_async(get_value, list(range(100)), callback=end_func)
        p.close()
        p.join()

        # p.map(get_value, list(range(100)))

# print("multiprocessing.cpu_count(): ", multiprocessing.cpu_count())
