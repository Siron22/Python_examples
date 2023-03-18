from threading import Thread

from L31.MR.common import full_path_files, grouping, counter_in_one_thread_for_multi


def letter_counter_in_n_threads(directory, letter_to_find, number_of_threads):
    files = full_path_files(directory)

    subgroups = grouping(files, number_of_threads)
    results = [{} for _ in range(len(subgroups))]
    threads = []
    for i, group in enumerate(subgroups):
        t = Thread(target=counter_in_one_thread_for_multi, args=(group, letter_to_find, results[i]))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    q = 0
    for item in results:
        q += item['value']

    return q