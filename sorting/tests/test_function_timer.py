from utils.function_timer import execution_time
from utils.random_sequence import get_random_sequence
from algorithms.bubble_sort import bubble_sort
from algorithms.selection_sort import selection_sort
from algorithms.merge_sort import merge_sort


def test_execution_time():
    collection = get_random_sequence(4000)

    assert execution_time(bubble_sort, collection) > 0
    assert execution_time(selection_sort, collection) > 0
    assert execution_time(merge_sort, collection) > 0
