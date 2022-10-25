from utils.reader import get_text, get_words, get_alphabet_length


def test_get_text():
    contents = get_text()
    assert contents


def test_get_words():
    text = get_text()
    assert len(get_words(text, 100)) == 100
    assert len(get_words(text, 1000)) == 1000


def test_get_alphabet_length():
    length = get_alphabet_length(get_text())
    assert length > 32