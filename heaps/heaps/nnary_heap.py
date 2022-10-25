import sys


class NnaryHeap:
    def __init__(self, initial_elements: list, n: int) -> None:
        self.__elements = []
        self.__n = n

        for element in initial_elements:
            self.__elements.append(element)

        self.__heapify()

    def n(self) -> int:
        return self.__n

    def elements(self) -> list:
        return self.__elements

    def elements_count(self) -> int:
        return len(self.__elements)

    def insert(self, value: int) -> None:
        self.__elements.append(value)
        self.__heapify()

    def remove_root(self) -> None:
        if self.elements_count() > 1:
            self.__elements[0] = self.__elements[-1]
            self.__elements.pop()
            self.__heapify_subtree(0)
        else:
            self.__elements.pop()

    def __heapify_subtree(self, index: int) -> None:
        largest_index = index

        children_indexes = []

        for i in range(self.__n):
            children_indexes.append(self.__n * index + i + 1)

        for i in children_indexes:
            if (
                i < self.elements_count()
                and self.__elements[largest_index] < self.__elements[i]
            ):
                largest_index = i

        if largest_index != index:
            self.__elements[index], self.__elements[largest_index] = (
                self.__elements[largest_index],
                self.__elements[index],
            )
            self.__heapify_subtree(largest_index)

    def __heapify(self) -> None:
        if self.elements_count() > 0:
            for i in range(self.elements_count() // self.__n - 1, -1, -1):
                self.__heapify_subtree(i)

    def print(self, node_index=0, depth=0):
        if node_index >= len(self.__elements):
            return
        for i in range(depth):
            sys.stdout.write("\t")
        print(self.__elements[node_index])
        for i in range(self.__n):
            self.print(node_index * self.__n + 1 + i, depth + 1)


if __name__ == "__main__":
    input_list = [3, 9, 2, 1, 4, 5]
    result_list = [9, 4, 5, 1, 3, 2]
    heap = NnaryHeap(input_list, 2)
