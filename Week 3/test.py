import string

def getAvailableLetters(lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    alphabet = string.ascii_lowercase
    
    for element in lettersGuessed:
        alphabet = alphabet.replace(element, '')
                
    return alphabet