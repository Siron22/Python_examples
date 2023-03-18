from L31.MR.common import full_path_files, count_in_file


def letter_counter_in_one_thread(directory, letter_to_find):
    letter_number = 0
    for file in full_path_files(directory):
        letter_number += count_in_file(file, letter_to_find)
    return letter_number
