from email.encoders import encode_noop


def get_text() -> str:
    with open("pan-tadeusz.txt", encoding="utf-8") as f:
        contents = f.read()

    return contents


def get_words(text: str, amount: int) -> list:
    words = text.split()
    return words[:amount]


def get_alphabet_length(text: str) -> int:
    characters = []
    words = text.split()

    for word in words:
        for char in word:
            if char not in characters:
                characters.append(char)

    return len(characters)