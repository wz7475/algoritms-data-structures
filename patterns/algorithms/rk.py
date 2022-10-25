from typing import List


def find_rk(text: str, pattern: str) -> List[int]:

    occurrences = []
    pattern_len = len(pattern)
    text_len = len(text)

    if text_len == 0 or pattern_len == 0 or pattern_len > text_len:
        return []
    hash_pat = 0
    hash_txt = 0
    # Jak.o q wybieramy przeważnie taką liczbę pierwszą, że IOą mieści się akurat
    # w słowie komputera, co pozwala wykonywać wszystkie operacje arytmetyczne z pojedynczą
    # precyzją
    prime = 3121
    inner_char_index = 0
    char = 256

    # calc hash max (only letters with the highest code)
    # for i in range(length_pattern - 1):
    #     hash_max = (hash_max * char) % prime
    hash_max = pow(char, pattern_len - 1) % prime

    # calc hashes (256 * hash_pat,  256 ^ 2, 256 ^ 3 ...
    for i in range(pattern_len):
        hash_pat = (char * hash_pat + ord(pattern[i])) % prime
        hash_txt = (char * hash_txt + ord(text[i])) % prime

    # Slide the pattern over text one by one
    for i in range(text_len - pattern_len + 1):
        if hash_pat == hash_txt:
            # hashes match
            for inner_char_index in range(pattern_len):
                if text[i + inner_char_index] != pattern[inner_char_index]:
                    break
                else:
                    # letter matches so far - continue
                    inner_char_index += 1
            if inner_char_index == pattern_len:
                occurrences.append(i)

        if i < text_len - pattern_len:
            # remove leading digit (upper line), process trailing (lower line)
            hash_txt = (char * (hash_txt - ord(text[i]) * hash_max) +
                        ord(text[i + pattern_len])) % prime

            if hash_txt < 0:
                hash_txt = hash_txt + prime
    return occurrences