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
