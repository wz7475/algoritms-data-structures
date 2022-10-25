from algorithms.naive import find_naive


def test_naive_naive_typical():
    positions = find_naive("aababab", "ba")
    assert len(positions) == 2
    assert positions[0] == 2
    assert positions[1] == 4

    positions = find_naive("aaaa", "a")
    assert len(positions) == 4
    assert positions == list(range(4))


def test_naive_naive_empty():
    assert len(find_naive("", "abcd")) == 0
    assert len(find_naive("abcd", "")) == 0
    assert len(find_naive("", "")) == 0


def test_naive_naive_equal():
    positions = find_naive("abcde", "abcde")
    assert len(positions) == 1
    assert positions[0] == 0


def test_naive_naive_non_existing():
    assert len(find_naive("abc", "abcde")) == 0
    assert len(find_naive("abc", "def")) == 0
