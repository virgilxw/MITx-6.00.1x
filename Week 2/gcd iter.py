def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    GCD = 1
    for n in range(1,a+1) or n in range(1,b+1):
        if a % n == 0:
            if b% n == 0:
                GCD = n
                
    return GCD