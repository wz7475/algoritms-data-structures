from heaps.nnary_heap import NnaryHeap
from random import randint
import matplotlib.pyplot as plt
import gc
import time


class BenchmarkManager:
    def __init__(self) -> None:
        self.__elements = []

        for i in range(100000):
            self.__elements.append(randint(1, 300000))

    def init_benchmark(self) -> None:
        elements_amounts = [i * 10000 for i in range(1, 11)]
        binary_results, triary_results, quadrary_results = [], [], []

        for amount in elements_amounts:
            binary_results.append(self.__init_time(amount, 2))
            triary_results.append(self.__init_time(amount, 3))
            quadrary_results.append(self.__init_time(amount, 4))
        
        self.__draw_plot(elements_amounts, binary_results, triary_results, quadrary_results, "fill_benchmark.png")

    def remove_benchmark(self) -> None:
        elements_amounts = [i * 10000 for i in range(1, 11)]
        binary_results, triary_results, quadrary_results = [], [], []

        for amount in elements_amounts:
            binary_results.append(self.__remove_time(amount, 2))
            triary_results.append(self.__remove_time(amount, 3))
            quadrary_results.append(self.__remove_time(amount, 4))
        
        self.__draw_plot(elements_amounts, binary_results, triary_results, quadrary_results, "deletion_benchmark.png")

    def __draw_plot(
        self, x_values: list, binary_values: list, triary_values: list, 
        quadrary_values: list, figure_name: str
    ) -> None:

        plt.plot(x_values, binary_values, color="g", label="2-ary heap")
        plt.plot(x_values, triary_values, color="r", label="3-ary heap")
        plt.plot(x_values, quadrary_values, color="b", label="4-ary heap")
        plt.legend()
        plt.xticks(rotation=45, fontsize="small")
        plt.savefig(figure_name)
        plt.show()

    def __init_time(self, elements_amount: int, n_narity: int) -> float:
        gc_status = gc.isenabled()
        gc.disable()

        start = time.process_time()
        NnaryHeap(self.__elements[:elements_amount], n_narity)
        stop = time.process_time()

        if gc_status:
            gc.enable()

        return stop - start

    def __remove_time(self, amount: int, n_narity: int) -> float:
        heap = NnaryHeap(self.__elements, n_narity)

        gc_status = gc.isenabled()
        gc.disable()

        start = time.process_time()

        for i in range(amount):
            heap.remove_root()

        stop = time.process_time()

        if gc_status:
            gc.enable()

        return stop - start
