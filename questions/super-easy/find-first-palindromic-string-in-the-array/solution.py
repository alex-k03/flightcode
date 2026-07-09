def first_palindrome(words):
    for word in words:
        if word == word[::-1]:
            return word
    return ""
