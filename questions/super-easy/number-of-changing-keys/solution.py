def number_of_changing_keys(s):
    s = s.lower()
    changes = 0
    for i in range(1, len(s)):
        if s[i] != s[i - 1]:
            changes += 1
    return changes
