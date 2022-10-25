from copy import copy


def merge_sort(elements: list) -> list:
    elements_copy = copy(elements)
    midpoint = len(elements_copy) // 2
    elements_left = elements_copy[midpoint:]
    elements_right = elements_copy[:midpoint]

    if midpoint > 0:
        elements_left = merge_sort(elements_left)
        elements_right = merge_sort(elements_right)

    return merge(elements_left, elements_right)


def merge(elements_1: list, elements_2: list) -> list:
    result = []
    elements_left = copy(elements_1)
    elements_right = copy(elements_2)

    while elements_left and elements_right:
        if elements_left[0] < elements_right[0]:
            result.append(elements_left[0])
            elements_left.pop(0)
        else:
            result.append(elements_right[0])
            elements_right.pop(0)

    while elements_left:
        result.append(elements_left[0])
        elements_left.pop(0)

    while elements_right:
        result.append(elements_right[0])
        elements_right.pop(0)

    return result
