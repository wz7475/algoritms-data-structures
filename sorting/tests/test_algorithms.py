from algorithms.bubble_sort import bubble_sort
from algorithms.quick_sort import quick_sort
from algorithms.selection_sort import selection_sort
from algorithms.merge_sort import merge, merge_sort
from utils.random_sequence import get_random_sequence


# Tests for bubble sort

def test_bubble_sort():
    random_collection = get_random_sequence(1000)
    assert bubble_sort(random_collection) == sorted(random_collection)


# Tests for selection sort

def test_selection_sort():
    random_collection = get_random_sequence(1000)
    assert selection_sort(random_collection) == sorted(random_collection)


# Tests for merge

def test_merge():
    collection_1 = sorted(get_random_sequence(10))
    collection_2 = sorted(get_random_sequence(15))
    sorted_collection = merge(collection_1, collection_2)
    collection_1.extend(collection_2)
    assert sorted_collection == sorted(collection_1)


# Tests for merge sort

def test_merge_sort():
    random_collection = get_random_sequence(1000)
    sorted_collection = merge_sort(random_collection)
    assert sorted_collection == sorted(random_collection)


#  tests for quick sort

def test_quick_sort():
    random_collection = get_random_sequence(1000)
    sorted_collection = quick_sort(random_collection)
    assert sorted_collection == sorted(random_collection)
