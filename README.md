# GUESS WORD   <a name="top"></a>

Guess Word is a Python terminal game, wich runs in the mock terminal on Heroku.

Main objective of game that user have to try guess mystery word.

![multi screen](readmeimges/responsive.JPG)

The live link can be found here - [Guess word](https://guess-word-g.herokuapp.com/)

# Index
* [How to play Game](How-to-play-Game)
* [Features](Features)
* [Testing](Testing)
* [Bugs](Bugs)
* [Validator testing](Validator-testing)
* [Deployment](Deployment)

# How to play Game

Game will randomly select a Mystery Word.
You will have six chances to guess what it
is one letter at a time. 

# Features

* Welcome screen
  * Welcomes user
  * Print rules of the game
  * Ask user to imput name
![Welcome screen](readmeimges/welcomescreen.JPG)
 
* Latter input
  * Check for letter in mystery word
  * Check if latter has been guessed
  * Returns respond if letter in word or not
![Guess letter](readmeimges/guesslatter.JPG)
  
* Game outcome
  * Show user if word guessed correct
  * Show user if ran out of mistakes allowed
![Game outcome](readmeimges/endgame.JPG)
![Game outcome2](readmeimges/endgame2.JPG)
  
## Features left to implement
* Allow to input only one letter
* Allow to input only letters
* Allow user to choose play again or not after game finished

# Testing 
I have manually tested this project:
* Passed the code trough a PEP8
* Tested in my local terminal
* Input letters and checked if system respond as shown in images above

# Bugs
## Solved bugs
* Writing project i had incorrect Indentation what made program stop running. 
* After installing extension in gitpod that identifies indentation errors i was able to run program

## Remaining Bugs
* No Bugs that i aware of remaining

# Validator testing
* PEP8
 * No errors were returned from PEP8 only some warnings
![PEP8](readmeimges/pep8.JPG)
 
 # Deployment
 
 This project was deployed using mock terminal for Heroku.
 * Steps for deployment:
   * Fork or clone this repository
   * Create a new Heroku app
   * Set the buildbacks to Python and NodeJS in that order
   * Link the Heroku app to the repository
   * Click on Deploy

### [Go To Top](#top)
 


  
