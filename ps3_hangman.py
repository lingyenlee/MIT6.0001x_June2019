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
    correctGuess = []
    
    for letter in lettersGuessed:
        if letter in secretWord:
            correctGuess += letter
    
    if len(correctGuess) == len(secretWord):
        return True
    else:
        return False
        
#print(isWordGuessed('durian', ['h','a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u']))


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    word = ""
    for letter in secretWord:
        if letter in lettersGuessed:
            word += letter
        else:
            word += " _ "
    return word
#print(getGuessedWord("apple", ['e', 'i', 'k', 'p', 'r', 's']))

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    string_copy = string.ascii_lowercase
    for letter in lettersGuessed:
        if letter in string_copy:
            string_copy = string_copy.replace(letter, "")
    
    return string_copy

#print(getAvailableLetters(['e', 'i', 'k', 'p', 'r', 's']))

def statement(text):
    print(text)

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
    numGuesses = 8
    
    lettersGuessed = []
    allLettersGuessed = []
    
    print(secretWord)
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is", len(secretWord), "letters long.")
    
    while True:
       
       
           
        
        if numGuesses > 0:
            print("--------------------")
            print("You have", numGuesses, "guesses left.")
            availableLetters = getAvailableLetters(lettersGuessed)
            print("Available letters:", availableLetters )
            guess = input("Please guess a letter: ")
            guessInLowerCase = guess.lower()
#           check the letter guessed, if not guessed, add to lettersGuessed
            if guessInLowerCase not in lettersGuessed:
                lettersGuessed.append(guessInLowerCase)
#                
#                    print("Sorry, you ran out of guesses. The word was", secretWord )
#                    break
#           check if word is guessed, if guessed, end game
            isGuessed = isWordGuessed(secretWord, lettersGuessed)
            if isGuessed:
                print("Good guess:", getGuessedWord(secretWord, lettersGuessed)),  
                print("----------------")
                return statement("Congratulations, you won!"),
                break
            

                #           if letter already guessed  
            elif guessInLowerCase in allLettersGuessed:
                 print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed)) 


#           check if letter guessed in secret word
            elif guessInLowerCase in secretWord:
                print("Good guess:", getGuessedWord(secretWord, lettersGuessed))        

#           check if letter guessed is in secret word, if not, minus 1 guess
            elif guessInLowerCase not in secretWord: 
                if numGuesses == 0:
                    return statement("Sorry, you ran out of guesses. The word was", secretWord )
                    break
                else:
                    numGuesses -= 1
                    print("Oops! That letter is not in my word:", getGuessedWord(secretWord, lettersGuessed))


#       if exceed number of guess, end game and reveal correct word
        else:
            
            return statement("Sorry, you ran out of guesses. The word was", secretWord )
            break
        
        allLettersGuessed.append(guessInLowerCase)
    
    

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
