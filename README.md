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
