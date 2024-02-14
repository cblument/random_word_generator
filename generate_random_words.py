#!/usr/bin/env python
'''Generate Random Words'''
from random import randint
from time import sleep
from sys import stdout
from random_word import RandomWords

def main():
    '''Random words'''
    r = RandomWords()
    while True:
        sleep_seconds = randint(1, 30)
        number_of_words = randint(2,9)
        words = []
        for x in range(number_of_words):
            words.append(r.get_random_word())
        stdout.write(' '.join(words)+ '\n')
        sleep(sleep_seconds)

if __name__ == '__main__':
    main()
