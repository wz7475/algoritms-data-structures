def find_naive(text: str, pattern: str) -> list:
    positions = []
    text_len = len(text)
    pattern_len = len(pattern)

    if text_len > 0 and pattern_len > 0:
        for i in range(text_len - pattern_len + 1):
            if text[i:i + pattern_len] == pattern:
                positions.append(i)

    return positions