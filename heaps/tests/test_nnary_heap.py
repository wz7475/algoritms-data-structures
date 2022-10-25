from heaps.nnary_heap import NnaryHeap


def test_heapify_binary():
    input_list = [3, 9, 2, 1, 4, 5]
    result_list = [9, 4, 5, 1, 3, 2]
    heap = NnaryHeap(input_list, 2)
    assert heap.elements() == result_list

def test_heapify_3nary():
    input_list = [19, 18, 38, 20, 36, 29, 28, 25, 22, 27, 21, 11, 6, 3, 9]
    result_list = [38, 36, 28, 25, 29, 27, 21, 19, 18, 22, 20, 11, 6, 3, 9]
    heap = NnaryHeap(input_list, 3)
    assert heap.elements() == result_list

def test_heapify_4nary():
    input_list = [19, 18, 38, 20, 36, 29, 28, 25, 22, 27, 21, 11, 6, 3, 9]
    result_list = [38, 29, 27, 20, 36, 18, 28, 25, 22, 19, 21, 11, 6, 3, 9]
    heap = NnaryHeap(input_list, 4)
    assert heap.elements() == result_list


def test_insert():
    input_list = [3, 9, 2, 1, 4, 5]
    heap = NnaryHeap(input_list, 2)
    heap.insert(7)

    assert heap.elements() == [9, 4, 7, 1, 3, 2, 5]


def test_remove_root():
    input_list = [3, 9, 2, 1, 4, 5]
    heap = NnaryHeap(input_list, 2)
    heap.remove_root()

    assert heap.elements() == [5, 4, 2, 1, 3]
