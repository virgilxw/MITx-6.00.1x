# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 12:07:17 2016

@author: Reuben
"""

low = 0
high = 100
guessCorrect = False

print ("Please think of a number between 0 and 100!")

while guessCorrect == False:
    guess = int( (low + high) / 2)
    print ("Is your secret number " + str(guess) + "?")
    answer = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    
    if answer == "c":
        print ("Game over. Your secret number was:", str(guess))
        guessCorrect = True
    elif answer == "h":
        high = guess
    elif answer == "l":
        low = guess
    else:
        print ("error: input was " + str(guess) + ". Only h,l,j accepted")
        