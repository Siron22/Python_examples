import os


def full_path_files(directory):
    """Returns list of full paths for files in directory"""
    files = os.listdir(directory)
    full_paths = []
    for file in files:
        full_paths.append(os.path.join(directory, file))
    return full_paths


def count_letter(content: str, letter):
    """Counts number of specified letter in content"""
    return content.count(letter)


def grouping(group: list, n: int):
    """Split group into n "almost equal" subgroups (groups could differ in 1)
    :return: list of subgroups
    """
    subgroups = []
    len_lst = len(group)
    if n >= len_lst:
        subgroups = [[i] for i in group]  # if number of subgroups more than items in group, place every item to separate subgroup
    else:
        items_in_sub_group_float = len_lst / n  # calculate approximate number of items in subgroup
        items_in_sub_group = int(items_in_sub_group_float)
        total_items_minus = items_in_sub_group * n
        delta = len_lst - total_items_minus  # how many items are not distributed among groups

        subgroups_sizes = [items_in_sub_group for _ in range(n)]  # initial subgroups sizes
        for i in range(delta):
            subgroups_sizes[i] += 1  # add not distributed items to first 'delta' subgroups by 1

        init_index = 0
        for size in subgroups_sizes:
            item = group[init_index: init_index + size]
            subgroups.append(item)
            init_index += size

    return subgroups


def count_in_file(file_path, letter):
    with open(file_path, 'r') as f:
        content = f.read()
    result = count_letter(content, letter=letter)
    return result


def counter_in_one_thread_for_multi(group_of_files, letter_to_find, output={}):
    letter_number = 0
    for file in group_of_files:
        letter_number += count_in_file(file, letter_to_find)
    output['value'] = letter_number
    return letter_number
