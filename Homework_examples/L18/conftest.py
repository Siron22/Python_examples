import sys
sys.path.append(r'D:\Development\Python\HillelAL')

import pytest

from Autumn2022.HW_download.L18.structure_without_list import StructureWithoutList


@pytest.fixture()
def empty_structure():
    return StructureWithoutList()


@pytest.fixture()
def structure_of_4_elements_index_at_the_end():
    struct = StructureWithoutList()
    struct.add(1)
    struct.add(2)
    struct.add(3)
    struct.add(4)
    return struct


@pytest.fixture()
def structure_of_4_elements_index_on_the_second_item():
    struct = StructureWithoutList()
    struct.add(1)
    struct.add(2)
    struct.add(3)
    struct.add(4)
    struct.get(2)
    return struct
