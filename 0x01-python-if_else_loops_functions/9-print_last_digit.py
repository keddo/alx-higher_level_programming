#!/usr/bin/python3
def print_last_digit(number):
    """Print the last digit of a number and return it"""
    return (number % 10) if number > 0 else (abs(number) % 10)
