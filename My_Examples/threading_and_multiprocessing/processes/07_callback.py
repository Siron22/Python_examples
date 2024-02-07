import multiprocessing


def end_func(response):
    print("response", response)


def out(x):
    print(f"value - {x}")
    return x


if __name__ == "__main__":
    with multiprocessing.Pool(multiprocessing.cpu_count() * 3) as p:
        for i in range(10):
            p.apply_async(out, args=(i,), callback=end_func)
        p.close()
        p.join()
