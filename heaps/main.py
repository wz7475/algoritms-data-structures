from utils.benchmark import BenchmarkManager
from heaps.nnary_heap import NnaryHeap


def main():
    mgr = BenchmarkManager()

    print("Note: close the active chart in order to continue benchmark.")

    print("Beginning heap fill time benchmark...")
    mgr.init_benchmark()

    print("Beginning multiple heap root deletion time benchmark...")
    mgr.remove_benchmark()

    print("Printing sample binary heap...")


if __name__ == "__main__":
    main()
