from algorithms.naive import find_naive
from algorithms.kmp import find_kmp
from algorithms.rk import find_rk
from utils.reader import get_text, get_words
import matplotlib.pyplot as plt
import time
import gc


class BenchmarkManager:
    def __init__(self) -> None:
        self.__text = get_text()

    def benchmark(self) -> None:
        amounts = [i * 100 for i in range(1, 11)]  # TODO: check the performance, naive is extremely slow
        naive_times, kmp_times, rk_times = [], [], []

        for amount in amounts:
            naive_times.append(self.__find_time(amount, find_naive))
            kmp_times.append(self.__find_time(amount, find_kmp))
            rk_times.append(self.__find_time(amount, find_rk))

        self.__draw_plot(amounts, naive_times, kmp_times, rk_times)

    def __draw_plot(
            self, x_amounts: list, y_naive: list, y_kmp: list, y_rk: list
        ) -> None:

        plt.plot(x_amounts, y_naive, color="r", label="Naive")
        plt.plot(x_amounts, y_kmp, color="g", label="KMP")
        plt.plot(x_amounts, y_rk, color="b", label="RK")
        plt.xticks(fontsize="small", rotation=45)
        plt.legend()
        plt.title("Pattern search time comparison")
        plt.show()
        plt.savefig("plot_linux.png")

    def __find_time(self, words_amount: int, function) -> float:
        patterns = get_words(self.__text, words_amount)

        gc_status = gc.isenabled()
        gc.disable()
        start = time.process_time()

        for pattern in patterns:
            function(self.__text, pattern)

        stop = time.process_time()
        if gc_status:
            gc.enable()

        return stop - start
