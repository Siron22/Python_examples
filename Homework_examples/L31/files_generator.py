import os
import random
import string

symbols = string.ascii_letters + string.digits + string.punctuation + string.whitespace


def file_generator(directory, number_of_files, size):
    for i in range(number_of_files):
        print(i)
        file_path = os.path.join(directory, f"file_{i}.txt")
        content = ''.join([random.choice(symbols) for _ in range(random.randint(size//2, size))])
        with open(file_path, 'w') as f:
            f.write(content)

#file_generator('files', 200, 1000_000)
