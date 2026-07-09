def first_unique_character_in_a_string(s):
    counts = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1

    for i, ch in enumerate(s):
        if counts[ch] == 1:
            return i
    return -1
