# Write a Python function to check whether a string is pangram or not. (Assume
# the string passed in does not have any punctuation)
# Note: Pangrams are words or sentences containing every letter of the
# alphabet at least once. For example: "The quick brown fox jumps over the
# lazy dog"

import string

def is_pangram():
    # Get input from the user
    s = input("Enter a sentence: ")
    
    # Create a set of all lowercase alphabets
    alphabet = set(string.ascii_lowercase)
    
    # Remove spaces and convert the string to lowercase
    s = s.replace(" ", "").lower()
    
    # Create a set of all unique letters in the input string
    input_letters = set(s)
    
    if alphabet.issubset(input_letters):
        print("The sentence is a pangram.")
    else:
        print("The sentence is not a pangram.")

is_pangram()
