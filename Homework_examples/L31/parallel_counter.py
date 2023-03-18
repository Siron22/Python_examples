from multiprocessing import Process, Manager

from L31.MR.common import full_path_files, grouping, counter_in_one_thread_for_multi


def letter_counter_in_n_processes(directory, letter_to_find, number_of_processes):
    files = full_path_files(directory)

    subgroups = grouping(files, number_of_processes)

    manager = Manager()
    results = [manager.dict() for _ in range(len(subgroups))]

    processes = []
    for i, group in enumerate(subgroups):
        process = Process(target=counter_in_one_thread_for_multi, args=(group, letter_to_find, results[i]))
        processes.append(process)
        process.start()

    for p in processes:
        p.join()

    q = 0
    for item in results:
        q += item['value']

    return q
