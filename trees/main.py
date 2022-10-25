from utils.benchmark import BenchmarkManager
from trees.bst import BST
from trees.avl import AVLTree


def main():
    print("Initializing benchmarks...")
    mgr = BenchmarkManager()

    print("Starting fill time benchmark...")
    mgr.fill_benchmark()

    print("Starting search time benchmark...")
    mgr.find_benchmark()

    print("Starting deletion time benchmark...")
    mgr.delete_benchmark()

    print_trees()


def print_trees():
    values = [10, 5, 2, 12, -45, 0, 18, -4, -7, -6, 13]
    bst = BST(values[0])
    bst.fill(values[1:])
    avl = AVLTree(values)

    print("\nPrinted BST:\n")
    print(f"{str(bst)}\n")

    print("\nPrinted AVL:\n")
    print(str(avl))


if __name__ == "__main__":
    main()
