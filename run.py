import random

print("Welcome to word guessing game!")
players_name = input("Before we start please tell me your name: ")
print("\n")
print("Hello, " + players_name + " and best of luck!")

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
word_underscore = word_underscore()
print(word_underscore)

mistakes_allowed = 6
letters_guessed = []
word_guessed = list(word_underscore)

while mistakes_allowed > 0:
    print("You only allowed " + str(mistakes_allowed) + " mistakes")
    guess = input("Please " + players_name + " guess letter: ").upper()
    if guess in letters_guessed:
        print("You alredy guessed the letter", guess)
    elif guess not in word:
        print(guess, " is not in the word.")
        mistakes_allowed -= 1
        letters_guessed.append(guess)
    else:
        print("Weldone " + players_name + " " + guess + " is in the word.")
        for i in range(len(word)):
            if list(word)[i] == guess:
                word_guessed[i] = guess
        print(''.join(word_guessed))
        letters_guessed.append(guess)
        
    if ''.join(word_guessed) == word:
        print("Congratulations! " + players_name + " you guessed the word!")
        break
        
