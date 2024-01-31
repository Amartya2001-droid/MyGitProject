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
