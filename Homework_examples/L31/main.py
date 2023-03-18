import time

from L31.MR.multi_thread_counter import letter_counter_in_n_threads
from L31.MR.one_thread_counter import letter_counter_in_one_thread
from L31.MR.parallel_counter import letter_counter_in_n_processes

dir_with_files = 'files'
letter = 'Q'
number_of_threads = 13
number_of_processes = 16

start_time = time.perf_counter_ns()
result_1 = letter_counter_in_one_thread(dir_with_files, letter)
end_time = time.perf_counter_ns()
print(result_1)
print(f"Function in one thread is executed in {(end_time - start_time)/1000_000} ms")
print()

start_time = time.perf_counter_ns()
result_2 = letter_counter_in_n_threads(dir_with_files, 'Q', number_of_threads)
end_time = time.perf_counter_ns()
print(result_2)
print(f"Function in {number_of_threads} threads is executed in {(end_time - start_time)/1000_000} ms")
print()

start_time = time.perf_counter_ns()
result_3 = letter_counter_in_n_processes(dir_with_files, 'Q', number_of_processes)
end_time = time.perf_counter_ns()
print(result_3)
print(f"Function in {number_of_processes} processes is executed in {(end_time - start_time)/1000_000} ms")
