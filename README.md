# MyGitProject
Assignment 2
Date: 29 Jan 2024

Amartya Karmakar created the Fibonacci series 
def fibonacci(n):
    """
    Generate the first n numbers of the Fibonacci sequence code.
    """
    sequence = []
    a, b = 0, 1
    while len(sequence) < n:
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Example: Get the first 10 numbers of the Fibonacci sequence
fibonacci_sequence = fibonacci(10)
fibonacci_sequence

Amartya Karmakar created the Palindrome check code.
def fibonacci(n):
    """
    Generate the first n numbers of the Fibonacci sequence.
    """
    sequence = []
    a, b = 0, 1
    while len(sequence) < n:
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Example: Get the first 10 numbers of the Fibonacci sequence
fibonacci_sequence = fibonacci(10)
fibonacci_sequence

Updated Fibonacci.py by creating a branch(not merged yet)
def fibonacci(n):
    """
    Generate the first n numbers of the Fibonacci sequence.

    Parameters:
    n (int): The number of elements in the Fibonacci sequence to generate. Must be a non-negative integer.

    Returns:
    list: A list containing the first n numbers of the Fibonacci sequence.

    Example:
    >>> fibonacci(10)
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer")

    sequence = []
    a, b = 0, 1
    while len(sequence) < n:
        sequence.append(a)
        a, b = b, a + b
    return sequence

def fibonacci_recursive(n):
    """ Recursive version of the Fibonacci function. Less efficient but useful for educational purposes. """
    if n <= 0:
        return []
        elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        seq = fibonacci_recursive(n-1)
        seq.append(seq[-1] + seq[-2])
        return seq

def test_fibonacci():
    """ Unit tests for the fibonacci function. """
    assert fibonacci(0) == []
    assert fibonacci(1) == [0]
    assert fibonacci(2) == [0, 1]
    assert fibonacci(5) == [0, 1, 1, 2, 3]
    print("All tests passed!")

if __name__ == "__main__":
    # Example usage
    fibonacci_sequence = fibonacci(10)
    print("Fibonacci Sequence:", fibonacci_sequence)

    # Run tests
    test_fibonacci()

# Aryan created a palindrome series which checks the strring reverse 
    #this is for Palindrome 
#created by aryan#

def checkif_palindrome(x):
	return x == x[::-1]

x = "madam"
Final = checkif_palindrome(x)

if Final:
	print("Yes")
else:
	print("No")
 
# Saim Sohail added a new functionality with palindrome3 for checking palindromes with more detailed error handling and input validation.

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
