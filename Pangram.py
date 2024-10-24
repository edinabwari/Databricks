# Write a Python function to check whether a string is pangram or not. (Assume
# the string passed in does not have any punctuation)
# Note: Pangrams are words or sentences containing every letter of the
# alphabet at least once. For example: "The quick brown fox jumps over the
# lazy dog"

import string

def is_pangram():
   
    sentence = input("Enter a sentence: ")
    alphabet = set(string.ascii_lowercase)
    sentence  = sentence .replace(" ", "").lower()
    
    input_letters = set(sentence )
    
    if alphabet.issubset(input_letters):
        print("The sentence is a pangram.")
    else:
        print("The sentence is not a pangram.")

is_pangram()
