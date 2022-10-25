import matplotlib.pyplot as plt
import gc
import time
import sys

from trees.bst import BST
from trees.avl import AVLTree
from random import randint


class BenchmarkManager:
    def __init__(self) -> None:
        sys.setrecursionlimit(10000)
        self.__initial_numbers = []

        while len(self.__initial_numbers) < 10000:
            number = randint(-30000, 30000)

            if number not in self.__initial_numbers:
                self.__initial_numbers.append(number)

        self.__bst = BST(self.__initial_numbers[0])
        self.__bst.fill(self.__initial_numbers[1:])
        self.__avl = AVLTree(self.__initial_numbers)

    # Getters

    def bst(self) -> BST:
        return self.__bst

    def avl(self) -> AVLTree:
        return self.__avl

    # Public methods

    def fill_benchmark(self) -> None:
        elements_amount = [i * 1000 for i in range(1, 11)]
        results_bst = []
        results_avl = []

        for amount in elements_amount:
            bst = BST(self.__initial_numbers[0])
            results_bst.append(
                self.__execution_time(bst.fill, self.__initial_numbers[1:amount])
            )

            results_avl.append(
                self.__avl_init_exec_time(self.__initial_numbers[:amount])
            )

        self.__draw_plot(elements_amount, results_bst, results_avl, "Fill time coparison")

    def find_benchmark(self) -> None:
        elements_amount = [i * 1000 for i in range(1, 11)]
        results_bst = []
        results_avl = []

        for amount in elements_amount:
            results_bst.append(self.__execution_time(self.__find_numbers_bst, amount))
            results_avl.append(self.__execution_time(self.__find_numbers_avl, amount))

        self.__draw_plot(elements_amount, results_bst, results_avl, "Search time comparison")

    def delete_benchmark(self) -> None:
        elements_amount = [i * 1000 for i in range(1, 11)]
        results_bst = []
        results_avl = []

        for amount in elements_amount:
            results_bst.append(self.__execution_time(self.__delete_numbers_bst, amount))
            results_avl.append(self.__execution_time(self.__delete_numbers_avl, amount))

            self.__bst = BST(self.__initial_numbers[0])
            self.__bst.fill(self.__initial_numbers[1:])
            self.__avl = AVLTree(self.__initial_numbers)

        self.__draw_plot(elements_amount, results_bst, results_avl, "Deletion time comparison")

    # Private methods

    def __draw_plot(
        self, x_values: list, bst_y: list, avl_y: list, title: str
    ) -> None:

        plt.plot(x_values, bst_y, label="BST", color="g")

        if avl_y is not None:
            plt.plot(x_values, avl_y, label="AVL", color="b")

        plt.title(title)
        plt.legend()
        plt.show()
        # plt.savefig(title + ".png")

    def __execution_time(self, function, argument) -> float:
        gc_status = gc.isenabled()
        gc.disable()

        start = time.process_time()
        function(argument)
        stop = time.process_time()

        if gc_status:
            gc.enable()

        return stop - start

    def __avl_init_exec_time(self, initial_numbers: list) -> float:
        gc_status = gc.isenabled()
        gc.disable()

        start = time.process_time()
        AVLTree(initial_numbers)
        stop = time.process_time()

        if gc_status:
            gc.enable()

        return stop - start

    def __find_numbers_bst(self, numbers_amount: int) -> None:
        for number in self.__initial_numbers[1:numbers_amount]:
            self.__bst.find(number)

    def __find_numbers_avl(self, numbers_amount: int) -> None:
        for number in self.__initial_numbers[:numbers_amount]:
            self.__avl.search(number)

    def __delete_numbers_bst(self, numbers_amount: int) -> None:
        for number in self.__initial_numbers[1:numbers_amount]:
            try:
                self.__bst.remove(number)
            except Exception:
                continue

    def __delete_numbers_avl(self, numbers_amount: int) -> None:
        for number in self.__initial_numbers[:numbers_amount]:
            self.__avl.delete(number)    
