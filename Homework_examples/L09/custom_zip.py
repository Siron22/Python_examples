from typing import Iterable, List, Tuple


"""
Написать функцию, которая принимает несколько итерируемых объектов, и возвращает список из кортежей составленных из элементов итерируемых объектов одного индекса.
Функция также должна принимать параметры с дефолтными значения:
full=False - по умолчанию "склеить" послдовательности по кратчайшей, иначе по самой длинной
default=None - если full=True, вместо недостающих элементов поставить значение указанное в параметре default
seq1 = [1, 2, 3, 4, 5]
seq2 = [9, 8, 7]
custom_zip(seq1, seq2) -> [(1, 9), (2, 8), (3, 7)]
result3 = custom_zip(seq1, seq2, full=True, default="Q") -> [(1, 9), (2, 8), (3, 7), (4, 'Q'), (5, 'Q')]

def custom_zip(*sequences: Iterable, full=False, default=None) -> List[List]:
    pass

"""


def custom_zip(*sequences: Iterable, full=False, default=None) -> List[Tuple]:
    result = []
    if full:
        result_length = max(map(len, sequences))
    else:
        result_length = min(map(len, sequences))

    for i in range(result_length):
        item = []
        for sequence in sequences:
            if len(sequence) > i:
                item.append(sequence[i])
            else:
                item.append(default)
        result.append(tuple(item))
    return result


seq1 = [1,    2, 3, 4, 5]
seq2 = [9,    8, 7]
seq3 = ['a', 'b']
seq4 = [0,    0, 0, 0]


assert custom_zip(seq1, seq2) == [(1, 9), (2, 8), (3, 7)]
assert custom_zip(seq2, seq1) == [(9, 1), (8, 2), (7, 3)]

assert custom_zip(seq1, seq2, full=True) == [(1, 9), (2, 8), (3, 7), (4, None), (5, None)]
assert custom_zip(seq2, seq1, full=True) == [(9, 1), (8, 2), (7, 3), (None, 4), (None, 5)]  # FAIL

assert custom_zip(seq1, seq2, full=True, default="Q") == [(1, 9), (2, 8), (3, 7), (4, 'Q'), (5, 'Q')]
assert custom_zip(seq2, seq1, full=True, default="Q") == [(9, 1), (8, 2), (7, 3), ('Q', 4), ('Q', 5)]

assert custom_zip(seq1, seq2, seq3, full=True) == [(1, 9, 'a'), (2, 8, 'b'), (3, 7, None), (4, None, None), (5, None, None)]

assert custom_zip(seq1, seq2, seq3, seq4, full=True, default='Q') == [(1, 9, 'a', 0), (2, 8, 'b', 0), (3, 7, 'Q', 0), (4, 'Q', 'Q', 0), (5, 'Q', 'Q', 'Q')]
assert custom_zip(seq3, seq2, seq1, seq4, full=True, default='Q') == [('a', 9, 1, 0), ('b', 8, 2, 0), ('Q', 7, 3, 0), ('Q', 'Q', 4, 0), ('Q', 'Q', 5, 'Q')]
