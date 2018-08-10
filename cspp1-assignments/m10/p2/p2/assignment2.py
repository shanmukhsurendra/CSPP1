'''
Exercise : Assignment-2
implement the function hangman, which takes one parameter - the secretWord
the user is to guess. This starts up an interactive game of Hangman between
the user and the computer. Be sure you take advantage of the three helper functions,
is_wordguessed, get_guessedword, and get_availableletters,
that you've defined in the previous part.
'''

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

wordlist_filename = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # in_file: file
    in_file = open(wordlist_filename, 'r')
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    print("  ", len(word_list), "words loaded.")
    return word_list

def choose_word(word_list):
    """
    word_list (list): list of words (strings)

    Returns a word from word_list at random
    """
    return random.choice(word_list)

# end of helper code
# -----------------------------------

# Load the list of words into the variable word_list
# so that it can be accessed from anywhere in the program
word_list = load_words()


def is_wordguessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
    False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for i in secret_word:
        if i not in letters_guessed:
            return False
    return True




def get_guessedword(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    a_a = ""
    for i in secret_word:
        if i not in letters_guessed:
            a_a = a_a + "_"
        else:
            a_a = a_a + i
    return a_a




def get_availableletters(letters_guessed):
    '''
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    a_a = ""
    str_s = 'abcdefghijklmnopqrstuvwxyz'
    for i in str_s:
        if i not in letters_guessed:
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
    letters_guessed = []
    guess = 8
    win = 0
    while (guess > 0 and win != 1):
        print("-----------------------------------------------")
        print("you have", str(guess), "left")
        print("available letters", get_availableletters(letters_guessed))
        k = input("please enter a letter: ").split()
        print(k)
        if k[0] in letters_guessed:
            print("oops you have guessed that letter: ", get_guessedword(secret_word, letters_guessed))
        else:
            letters_guessed = letters_guessed + k
            if is_wordguessed(secret_word, k) == True:
                print("good guess", get_guessedword(secret_word, letters_guessed))
                if secret_word == get_guessedword(secret_word, letters_guessed):
                    win = 1
            else:
                print("that letter is  found", get_guessedword(secret_word, letters_guessed))
                guess -= 1
    if win == 1:
        print("you won ")
    else:
        print("sorry you are not eligible to guesss "+secret_word)









# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secret_word while you're testing)

# secret_word = choose_word(word_list).lower()
# hangman(secret_word)




def main():
    '''
    Main function for the given program
    When you've completed your hangman function, uncomment these two lines
    and run this file to test! (hint: you might want to pick your own
    secretWord while you're testing)
    '''
    secretWord = choose_word(word_list).lower()
    hangman(secretWord)


if __name__ == "__main__":
    main()
