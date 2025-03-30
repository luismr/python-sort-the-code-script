def sort_code(s):
    """
    Sort a string of unique alphabetic characters in alphabetical order.
    
    Args:
        s (str): Input string containing up to 26 unique alphabetic characters
        
    Returns:
        str: The sorted string in alphabetical order
    """
    # Convert string to list of characters, sort them, and join back to string
    return ''.join(sorted(s))

# Test cases
if __name__ == "__main__":
    test_cases = [
        "acbdfe",
        "pqksuvy"
    ]
    
    for test in test_cases:
        result = sort_code(test)
        print(f'Input: "{test}" => Output: "{result}"') 