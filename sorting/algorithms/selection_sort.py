from copy import copy


def selection_sort(elements: list) -> list:
    elements_copy = copy(elements)

    for i in range(len(elements_copy) - 1):
        parted_list = elements_copy[i + 1:]
        min_element = min(parted_list)
        min_element_index = parted_list.index(min_element) + i + 1

        if min_element < elements_copy[i]:
            elements_copy[i], elements_copy[min_element_index] = swap(
                elements_copy[i], elements_copy[min_element_index]
            )

    return elements_copy


def swap(x, y):
    temp = y
    y = x
    x = temp
    return x, y
