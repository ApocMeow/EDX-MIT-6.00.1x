# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 09:45:04 2016

@author: james.hussey
"""
guessed = False
high = 100
low = 0
# Intro statement
print("Please think of a number between 0 and 100!")
# Initial Guess

#while loop to keep things running
while guessed != True:
    guess = (high + low) // 2
    print("Is your secret number %s?" % guess)
    user_hint = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.").lower()
    # Code for invalid input
    if user_hint == 'c':
        print("Game over. Your secret number was: %s" % guess)
        guessed = True
    elif user_hint == 'h':
        high = int(guess)
    elif user_hint == 'l':
        low = int(guess)
    else:
        print("Sorry, I did not understand your input.")
    
    
