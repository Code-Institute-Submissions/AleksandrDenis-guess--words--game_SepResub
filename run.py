import random

def get_word(fname):
    word_list = open('wordlist.txt','r+')
    word = random.choice(word_list.read().split())
    return word.upper()
    