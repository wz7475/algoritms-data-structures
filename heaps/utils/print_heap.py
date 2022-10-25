from heaps.nnary_heap import NnaryHeap


def main():
    input_list = [19, 18, 38, 20, 36, 29, 28, 25, 22, 27, 21, 11, 6, 3, 9]
    heap3 = NnaryHeap(input_list, 3)
    heap3.print()
    print()

    heap2 = NnaryHeap(input_list, 2)
    heap2.print()
    print()

    heap4 = NnaryHeap(input_list, 4)
    heap4.print()
    print()


if __name__ == "__main__":
    main()