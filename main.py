import random
from sys import exit
import read_english_dictionary


words = read_english_dictionary.load_words()
tries = 10


def main():
    global tries,words
    while True:
        corr = random.choice(words)
        while tries > 0:
            print('_ ' * len(corr))
            word = input('please guess this word,enter q to exit: ')
            if word == 'q':
                exit()
            elif word == 'jump it':
                break
            elif word in words and len(word) == len(corr):
                print('correct! next word')
                break
            elif word in words:
                print('are you sure thats the same word?')
                tries -= 1
                print(tries,'more tries left')
            else:
                print('wrong!')
                tries -= 1
                print(tries, 'more tries left')
        tries = 10
        print(corr)
        print('\n\n\n\n\n')
        print('next word:')

if __name__ == '__main__':
    main()
