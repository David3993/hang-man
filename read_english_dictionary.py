def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = word_file.readlines()
        words = [word.strip() for word in valid_words]
    return words


if __name__ == '__main__':
    english_words = load_words()
    # demo print
    print('fate' in english_words)
