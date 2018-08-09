'''
Exercise : Assignment-2
implement the function hangman, which takes one parameter - the secretWord 
the user is to guess. This starts up an interactive game of Hangman between 
the user and the computer. Be sure you take advantage of the three helper functions, 
isWordGuessed, getGuessedWord, and getAvailableLetters, 
that you've defined in the previous part.
'''

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


def isWordGuessed(secret_word, lettersGuessed):
    '''
    secret_word: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secret_word are in lettersGuessed;
    False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for i in secret_word:
        if i not in lettersGuessed:
            return False
    return True




def getGuessedWord(secret_word, lettersGuessed):
    '''
    secret_word: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    a_a = ""
    for i in secret_word:
        if i not in lettersGuessed:
            a_a = a_a + "_"
        else:
            a_a = a_a + i
    return a_a




def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    a_a = ""
    str_s = 'abcdefghijklmnopqrstuvwxyz'
    for i in str_s:
        if i not in lettersGuessed:
            a_a = a_a + i
    return a_a

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secret_word contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is", str(len(secret_word)))
    lettersGuessed = []
    guess = 8
    win = 0
    while (guess > 0 and win != 1):
        print("-----------------------------------------------")
        print("you have", str(guess), "left")
        print("available letters", getAvailableLetters(lettersGuessed))
        k = input("please enter a letter: ").split()
        print(k)
        if k[0] in lettersGuessed:
            print("oops you have guessed that letter: ", getGuessedWord(secret_word, lettersGuessed))
        else:
            lettersGuessed = lettersGuessed + k
            if isWordGuessed(secret_word, k) == True:
                print("good guess", getGuessedWord(secret_word, lettersGuessed))
                if secret_word == getGuessedWord(secret_word, lettersGuessed):
                    win = 1
            else:
                print("that letter is  found", getGuessedWord(secret_word, lettersGuessed))
                guess -= 1
    if win == 1:
        print("you won ")
    else:
        print("sorry you are not eligible to guesss "+secret_word)









# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secret_word while you're testing)

# secret_word = chooseWord(wordlist).lower()
# hangman(secret_word)




def main():
    '''
    Main function for the given program
    
    When you've completed your hangman function, uncomment these two lines
    and run this file to test! (hint: you might want to pick your own
    secretWord while you're testing)
    '''
    secretWord = chooseWord(wordlist).lower()
    hangman(secretWord)


if __name__ == "__main__":
    main()
