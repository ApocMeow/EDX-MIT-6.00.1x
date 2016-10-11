# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    result = False
    if len(lettersGuessed) == 0:
            result = False 
    for l in secretWord:
        if l not in lettersGuessed:
            result = False
            break
        else:
            result = True
    return result

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    breakdown = ''
    for l in secretWord:
        if l not in lettersGuessed:
            breakdown += '_ '
        else:
            breakdown += l
    return breakdown


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for l in lettersGuessed:
        if l in alphabet:
            alphabet = alphabet.replace(l, '')
    return alphabet
    

             
def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE... 
    
    mistakesMade = 0
    lettersGuessed = []

    def getUserGuess(mistakesMade):
        '''
        This function is used to ask the user for their input
        and then handle that guess appropriately.
        '''
        guess = input('Please guess a letter: ')
        if len(guess) > 1:
            print('Guesses must be single letters!')
        elif guess in '1234567890':
            print('Guesses must be single letters!')
        else:
            if guess.lower() in lettersGuessed:
                print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
            else:
                lettersGuessed.append(guess.lower())
                if guess.lower() in secretWord:
                    print('Good Guess: ' + getGuessedWord(secretWord, lettersGuessed))
                else:
                    print('Oops! That letter is not in my word: ' + getGuessedWord(secretWord, lettersGuessed))
                    mistakesMade += 1
        return mistakesMade
    
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is %s letters long.' % len(secretWord))
    print('------------')
    while mistakesMade < 9:
        print('You have %s guesses left.' % (8 - mistakesMade))
        print('Available letters: ' + getAvailableLetters(lettersGuessed))
        mistakesMade = getUserGuess(mistakesMade)
        getAvailableLetters(lettersGuessed)
        print('------------')
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print('Congratulations, you won!')
            break
        elif mistakesMade == 8:
            print('Sorry, you ran out of guesses. The word was: ' + secretWord)
            break
        else:
            continue

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
