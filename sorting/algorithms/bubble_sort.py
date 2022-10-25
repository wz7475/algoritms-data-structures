from collections.abc import Sequence
from copy import copy


def bubble_sort(collection: Sequence):
    length = len(collection)
    collection_copy = copy(collection)
    for i in range(length):
        for j in range(1, length):
            if collection_copy[j - 1] > collection_copy[j]:
                collection_copy[j - 1], collection_copy[j] = collection_copy[j], collection_copy[j - 1]
    return collection_copy
