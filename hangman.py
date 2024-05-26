# hangman.py


# Hangman Game
# -----------------------------------

import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
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



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for char in secret_word:
        if char not in letters_guessed:
            return False

    return True



def get_guessed_word(secret_word, letters_guessed):

    word = ''
    for char in secret_word:
        if char in letters_guessed:
            word += char
        else:
            word += '_'

    return word




def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    available_letter =''
    for char in (string.ascii_lowercase):
        if char not in letters_guessed:
            available_letter+= char

    return available_letter

def total_score(guess,secret_word):
    unique_letter= len(set(secret_word))
    score= (guess+4)*unique_letter+ 3*(len(secret_word))
    return score
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    print("Welcome Hangman !")
    print(f"I am thinking of a word that is {len(secret_word)} letters long")
    print("----------------")

    vowels = 'aeiou'

    guess = 10
    letters_guessed = []

    while guess > 0:
        print(f"you have {guess} guess left.")
        print(f"Available letters {get_available_letters(letters_guessed)}")
        print("----------------")
        letter_guess = input("Please guess a letter :").lower()
        if not letter_guess.isalpha():
            print("Oops! That is not a valid letter. Please enter a valid letter from a alphabet.")
        elif len(letter_guess) != 1:
            print("Oops! That is not a valid letter. Please enter a valid letter from a alphabet.")
        else:
            letters_guessed.append(letter_guess)

            if letter_guess not in secret_word:
                print(f"oops the letter is not in my word :{get_guessed_word(secret_word, letters_guessed)}")
                if letter_guess in vowels:
                    guess -= 2
                else:
                    guess -= 1
            else:
                print(f"Good guess : {get_guessed_word(secret_word, letters_guessed)}")

            if is_word_guessed(secret_word, letters_guessed) == True:
                print(f"your_score is {total_score(guess, secret_word)}")
                print("Congratulations you won !")

                break

        if guess <= 0:
            print(f"Sorry, you ran out of guesses. The word was {secret_word}.")
            break





# -----------------------------------








    






if __name__ == "__main__":
  secret_word = choose_word(wordlist)
  hangman(secret_word)

###############
    
    
