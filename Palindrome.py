def is_palindrome(s):
    """
    Check if the given string is a palindrome.
    """
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_s = ''.join(char for char in s if char.isalnum()).lower()
    # Check if the string is equal to its reverse
    return cleaned_s == cleaned_s[::-1]

# Example: Check if the following strings are palindromes
test_strings = ["racecar", "hello", "Madam, I'm Adam"]
palindrome_check = {string: is_palindrome(string) for string in test_strings}
palindrome_check
