def find_words_containing_character(words, x):
    answer = []
    for i, word in enumerate(words):
        if x in word:
            answer.append(i)
    return answer
