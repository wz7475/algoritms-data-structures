from typing import List


def prefix_function(pattern: str) -> List[int]:
    pattern_length = len(pattern)
    lps = [0] * pattern_length

    character_index = 1
    previous_lps = 0

    while character_index < pattern_length:
        if pattern[character_index] == pattern[previous_lps]:
            # increment next value in lps if match
            previous_lps += 1
            lps[character_index] = previous_lps
            character_index += 1
        else:
            if previous_lps == 0:
                # simple case for B in "AB"
                lps[previous_lps] = 0
                character_index += 1
            else:
                # (we don't move character_index) we go back to last 0 (1 position for loop)
                previous_lps = lps[previous_lps - 1]

    return lps


def find_kmp(text: str, pattern: str) -> List[int]:
    lps = prefix_function(pattern)
    text_ptr = 0
    pattern_ptr = 0
    occurrences_indexes = []

    if len(text) == 0 or len(pattern) == 0 or len(pattern) > len(text):
        return []

    while text_ptr < len(text):
        if text[text_ptr] == pattern[pattern_ptr]:
            text_ptr += 1
            pattern_ptr += 1
        else:
            if pattern_ptr == 0:
                # we moved back lps pointer to last 0, so we need to move window
                text_ptr += 1
            else:
                # move back pattern_ptr at 1 (we save comparisons for a couple of fist characters)
                pattern_ptr = lps[pattern_ptr - 1]
        if pattern_ptr == len(pattern):
            occurrences_indexes.append(text_ptr - len(pattern))
            pattern_ptr = lps[pattern_ptr - 1]
    return occurrences_indexes

# pat[] = "AAA CAA AA"
# lps      012 012 33
# ind      012 345 67
