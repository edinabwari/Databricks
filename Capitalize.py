# Write a program that accepts a string as input, capitalizes the first letter of each
# word in the string, and then returns the result string.
# Examples:
# "hi"=> returns "Hi"
# "i love programming"=> returns "I Love Programming"

def capitalize(input_sentence):
    
    capitalized = input_sentence.title()
    return capitalized

user_input = input("Enter a sentence: ")
result = capitalize(user_input)
print(result)
