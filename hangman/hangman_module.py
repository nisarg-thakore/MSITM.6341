#  write code as a module accepting word and guessed letters
# This example code for hangman game onto sushma_practice_1
import random
# return the word

# define the list of the words
# get the random word from the given list as a test word
# define maximum attempts
listOfWords = ['github', 'agile', 'development', 'computing', 'information']
MaxAttemptsAllowed = 6

def get_word():
    return random.choice(listOfWords)

# if guessed letters are in the word, display the letter in that position of the word and remaining place mask as '_'
def IdentifyMissingLetters(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display+= letter
        else:
            display+= "_"
    return(display)

