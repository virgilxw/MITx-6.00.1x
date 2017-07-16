def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    
    if len(aStr) <= 1:
        if aStr == char:
            return True
        else:
            return False
            
    else:
        midPoint = int(len(aStr)/2)
        if aStr[midPoint] > char:
            return isIn(char, aStr[0:midPoint])
        else:
            return isIn(char, aStr[midPoint:])
            