#!/usr/bin/python3
def uppercase(str):
    """Print a string in uppercase."""
    upper_str = ''
    for char in str:
        if char >= 'a' and char <= 'z':
            upper_str += chr(ord(char) - 32)
        else:
            upper_str += char
    print(upper_str)
