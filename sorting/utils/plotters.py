from utils.filereader import read_contents
from utils.function_timer import execution_time
from algorithms.bubble_sort import bubble_sort
from algorithms.selection_sort import selection_sort
from algorithms.merge_sort import merge_sort
from algorithms.quick_sort import quick_sort

import matplotlib.pyplot as plt


def plot_all():
    print("Starting execution time survey for all..")

    elements_amount_x = [i * 1000 for i in range(1, 8)]
    words = read_contents().split()
    bubble_time_y, selection_time_y, merge_time_y, quick_time_y = [], [], [], []

    for amount in elements_amount_x:
        selected_words = words[:amount]

        bubble_time = execution_time(bubble_sort, selected_words)
        selection_time = execution_time(selection_sort, selected_words)
        merge_time = execution_time(merge_sort, selected_words)
        quick_time = execution_time(quick_sort, selected_words)

        bubble_time_y.append(bubble_time)
        selection_time_y.append(selection_time)
        merge_time_y.append(merge_time)
        quick_time_y.append(quick_time)

    plt.clf()
    plt.plot(elements_amount_x, bubble_time_y, color="r", label="Bubble sort")
    plt.plot(
        elements_amount_x, selection_time_y, color="g", label="Selection sort")
    plt.plot(elements_amount_x, merge_time_y, color="b", label="Merge sort")
    plt.plot(elements_amount_x, quick_time_y, color="y", label="Quick sort")

    plt.xlabel("Number of words")
    plt.ylabel("Execution time (in seconds)")

    plt.xticks(rotation=45, fontsize="small")

    plt.legend()
    plt.savefig("sorting_time_all.png")


def plot_merge_quick():
    print("Starting execution time survey for merge and quick...")

    elements_amount_x = [i * 1000 for i in range(1, 30)]
    words = read_contents().split()
    bubble_time_y, selection_time_y, merge_time_y, quick_time_y = [], [], [], []

    for amount in elements_amount_x:
        selected_words = words[:amount]

        merge_time = execution_time(merge_sort, selected_words)
        quick_time = execution_time(quick_sort, selected_words)

        merge_time_y.append(merge_time)
        quick_time_y.append(quick_time)

    plt.clf()
    plt.plot(elements_amount_x, merge_time_y, color="b", label="Merge sort")
    plt.plot(elements_amount_x, quick_time_y, color="y", label="Quick sort")

    plt.xlabel("Number of words")
    plt.ylabel("Execution time (in seconds)")

    plt.xticks(rotation=45, fontsize="small")

    plt.legend()
    plt.savefig("sorting_time_merge_quick.png")
