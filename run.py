import random

def get_word(fname):
    """
    Get word from list
    Choose random word 
    """
    word_list = open('wordlist.txt','r+')
    word = random.choice(word_list.read().split())
    return word.upper()
word = get_word('wordlist.txt')
print(word)

def word_underscore():
    """
    Show underscores
    Same length as mystery word
    """
    word_underscore = []
    for i in range(len(word)):
        word_underscore.append('_')
        return ''.join(word_underscore)