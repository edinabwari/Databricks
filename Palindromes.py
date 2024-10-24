# Write a Python function that checks whether a word or phrase is palindrome or
# not.
# Note: A palindrome is word, phrase, or sequence that reads the same
# backward as forward, e.g., madam,kayak,racecar, or a phrase "nurses run"

def is_palindrome():
    s = input("Enter a word or phrase: ")
    
    s = s.replace(" ", "").lower()
    
    if s == s[::-1]:
        print("It is a palindrome!")
    else:
        print("It is not a palindrome.")

is_palindrome()
