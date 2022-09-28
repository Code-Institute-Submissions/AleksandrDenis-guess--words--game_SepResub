import random
# greating
print("Welcome to word guessing game fruit edition!") 
print("----------------------------------------")
print("Game will randomly select a Mystery Word.\n",
      "You will have six chances to guess what it\n",
      "is one letter at a time.")
print("----------------------------------------")
players_name = input("Before we start. What should I call you?:\n ")
print("\n")
print("Hello, " + players_name + " your word is:")


def get_word(fname):
    """
    Get word from list 
    Choose random word 
    """
    word_list = open('wordlist.txt', 'r+')
    random_word = random.choice(word_list.read().split())
    return random_word.upper()


random_word = get_word('wordlist.txt')


def word_underscore():
    """
    Show underscores
    Same length as mystery word
    """
    word_underscore = []
    for i in range(len(random_word)):
        word_underscore.append('_')
    return ''.join(word_underscore)


word_underscore = word_underscore()
print(word_underscore)


def display_game(word_underscore):
    print()

mistakes_allowed = 6
letters_guessed = []
word_guessed = list(word_underscore)

while mistakes_allowed > 0:
    print("You only allowed " + str(mistakes_allowed) + " mistakes")
    print("\n")
    guess = input("Please " + players_name + " guess letter:\n ").upper()
    if guess in letters_guessed:
        print("You alredy guessed the letter", guess)
    elif guess not in random_word:
        print(guess, " is not in the word.")
        mistakes_allowed -= 1
        letters_guessed.append(guess)
    else:
        print("Weldone " + players_name + " " + guess + " is in the word.")
        for i in range(len(random_word)):
            if list(random_word)[i] == guess:
                word_guessed[i] = guess
        print(''.join(word_guessed))
        letters_guessed.append(guess)
    if ''.join(word_guessed) == random_word:
        print("Congratulations! " + players_name + " you guessed the word!")
        break
    elif mistakes_allowed == 0:
        print("Sorry, you ran out of tries. The word was " + random_word)        
