from copy import copy
from random import randint

from typing import Tuple


def quick_sort(elements: list) -> list:
    collection_copy = copy(elements)
    if len(collection_copy) < 2:
        return collection_copy
    else:
        pivot_index = randint(0, len(collection_copy) - 1)
        pivot = collection_copy[pivot_index]
        smaller, greater = find_smaller_bigger(collection_copy, pivot_index)
        return quick_sort(smaller) + [pivot] + quick_sort(greater)


def find_smaller_bigger(elements: list, pivot_index: int) -> Tuple[list, list]:
    smaller = []
    bigger = []
    for index, element in enumerate(elements):
        if index != pivot_index:
            if element <= elements[pivot_index]:
                smaller.append(element)
            else:
                bigger.append(element)
    return smaller, bigger
