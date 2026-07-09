def maximum_number_of_words_found_in_sentences(sentences):
    return max(len(sentence.split()) for sentence in sentences)
