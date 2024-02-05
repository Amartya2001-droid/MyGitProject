# ---------------------------------------------------
# Palindrome Checker with Error Handling
# Authored by: Saim Sohail
# ---------------------------------------------------

def palindrome3(input_string):
    # Checks if string is a palindrome ignoring cases, spaces, and non-alphanumeric chars

    # First, check if input is actually a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")  # If not, stop and tell the user

    cleaned_string = ""  # Prepare an empty string to fill with cleaned characters
    for character in input_string:  # Go through each character in the input
        if character.isalnum():  # Keep only letters and numbers
            cleaned_string += character.lower()  # Add them to cleaned_string in lowercase

    reverse_string = cleaned_string[::-1]  # Make a reversed version of cleaned_string

    # Now, check if cleaned_string is the same as reverse_string
    if cleaned_string == reverse_string:
        return True  # It is a palindrome
    else:
        return False  # It is not a palindrome

# Let's test our function with some examples
try:
    # "aeroplane" is not a palindrome because reversing it does not give the same word.
    print(palindrome3("aeroplane"))  # Expected to be false
    
    # "Hi, I'm Saim" is not a palindrome for similar reasons, it doesn't read the same backward and forward.
    print(palindrome3("Hi, I'm Saim"))    # Expected to be false
    
    # 12345 is not a string, so it will raise a TypeError before checking if it's a palindrome.
    # Additionally, even if it were treated as a string, it's not a palindrome.
    print(palindrome3(12345))  # This will raise an error
except TypeError as e:
    # This error message explains why 12345 causes an error.
    print("Error:", e)  # Show the error if input is not a string
