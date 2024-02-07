import multiprocessing


def end_func(response):
    print("response", response)


def out(x, y, z):
    print(f"value - {x}, {y}, {z}")
    return x, y, z


if __name__ == "__main__":
    with multiprocessing.Pool(multiprocessing.cpu_count() * 3) as p:
        p.starmap_async(out, [(1, 2, 3), (4, 5, 6), (7, 8, 9)], callback=end_func)
        p.wait() # заменяет p.close() и p.join() для async методов
        # p.close()
        # p.join()
