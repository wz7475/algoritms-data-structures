from random import randint
from collections.abc import Sequence


def get_random_sequence(length: int) -> Sequence:
    random_collection = []
    for i in range(length):
        random_collection.append(randint(-100, 100))
    return random_collection
