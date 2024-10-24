# Write a Python function that checks whether a word or phrase is palindrome or
# not.
# Note: A palindrome is word, phrase, or sequence that reads the same
# backward as forward, e.g., madam,kayak,racecar, or a phrase "nurses run"

def is_palindrome():
    text = input("Enter a Text : ")
    
    text = text.replace(" ", "").lower()
    
    if text == text[::-1]:
        print("The text is a palindrome")
    else:
        print("The text is not a palindrome.")

is_palindrome()
