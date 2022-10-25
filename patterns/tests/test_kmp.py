from algorithms.kmp import prefix_function, find_kmp


def test_kmp_prefix_function():
    pattern = "AAABAAA"
    lps = prefix_function(pattern)
    assert lps == [0, 1, 2, 0, 1, 2, 3]

    positions = find_kmp("aababab", "ba")
    assert len(positions) == 2
    assert positions[0] == 2
    assert positions[1] == 4

    positions = find_kmp("aaaa", "a")
    assert len(positions) == 4
    assert positions == list(range(4))


def test_kmp_naive_empty():
    assert len(find_kmp("", "abcd")) == 0
    assert len(find_kmp("abcd", "")) == 0
    assert len(find_kmp("", "")) == 0


def test_kmp_naive_equal():
    positions = find_kmp("abcde", "abcde")
    assert len(positions) == 1
    assert positions[0] == 0


def test_kmp_naive_non_existing():
    assert len(find_kmp("abc", "abcde")) == 0
    assert len(find_kmp("abc", "def")) == 0