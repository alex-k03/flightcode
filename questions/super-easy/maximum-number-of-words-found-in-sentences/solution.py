def most_words_found(sentences):
    return max(len(sentence.split()) for sentence in sentences)
