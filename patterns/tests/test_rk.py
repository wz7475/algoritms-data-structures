from algorithms.rk import find_rk


def test_rk_naive_typical():
    positions = find_rk("aababab", "ba")
    assert len(positions) == 2
    assert positions[0] == 2
    assert positions[1] == 4

    positions = find_rk("aaaa", "a")
    assert len(positions) == 4
    assert positions == list(range(4))


def test_rk_naive_empty():
    assert len(find_rk("", "abcd")) == 0
    assert len(find_rk("abcd", "")) == 0
    assert len(find_rk("", "")) == 0


def test_rk_naive_equal():
    positions = find_rk("abcde", "abcde")
    assert len(positions) == 1
    assert positions[0] == 0


def test_rk_naive_non_existing():
    assert len(find_rk("abc", "abcde")) == 0
    assert len(find_rk("abc", "def")) == 0