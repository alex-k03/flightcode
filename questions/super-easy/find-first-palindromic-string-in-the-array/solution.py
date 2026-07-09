def find_first_palindromic_string_in_the_array(words):
    for word in words:
        if word == word[::-1]:
            return word
    return ""
