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
    word_list = open('wordlist.txt', 'r+', encoding='UTF-8')
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
    """
    Print underscore lenght of the word
    """
    print()


def get_guess(fname):
    """
    allow only one letter at the time
    warn about letter already guessed
    allow only letters
    """
    while True:
        guess = input("Please " + players_name + " guess letter:\n ").upper()
        guess = guess.upper()
        if len(guess) != 1:
            print("Please only type one letter at the time.")
        elif guess in letters_guessed:
            print("You alredy guessed the letter", guess)
        elif not guess.isalpha():
            print("Only letters allowed.")
        else:
            return guess


MISTAKES_ALLOWED = 6
letters_guessed = []


def start_over():
    """
    allows restart game over
    """
    return input(
        "Do you want to play again? Press y for yes or any key for no"
        ).lower().startswith('y')


word_guessed = list(word_underscore)
GAME_OVER = False


while True:
    display_game(word_underscore)

    guess = get_guess(word_underscore)

    if MISTAKES_ALLOWED > 0:
        print(
            "You only allowed " + str(MISTAKES_ALLOWED)
            + " mistakes remaining.")

    if guess not in random_word:
        print(guess, "is not in the word.")
        MISTAKES_ALLOWED -= 1
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

    elif MISTAKES_ALLOWED == 0:
        print("Sorry, you ran out of tries. The word was " + random_word)
        GAME_OVER = True
    if GAME_OVER:
        if start_over():
            MISTAKES_ALLOWED = 6
            letters_guessed = []
            word_guessed = list(word_underscore)
            random_word = get_word('wordlist.txt')
            GAME_OVER = False
        else:
            break
