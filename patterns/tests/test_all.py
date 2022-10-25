from tests.test_naive import *
from tests.test_kmp import *
from tests.test_rk import *
from random import randint


def test_all():
    alphabet = ["a", "b"]
    random_text, random_pattern = "", ""

    for i in range(100):
        random_text += alphabet[randint(0, 1)]

    for i in range(4):
        random_pattern += alphabet[randint(0, 1)]

    assert (
        find_naive(random_text, random_pattern) 
        == find_kmp(random_text, random_pattern) 
        == find_rk(random_text, random_pattern)
    )
