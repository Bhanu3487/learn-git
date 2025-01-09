"""This module contains basic arithmetic operations and Euclid's algorithm for GCD."""

def add(a, b):
    """Returns the sum of a and b."""
    return a + b

def subtract(a, b):
    """Returns the difference between a and b."""
    return a - b  

def multiply(a, b):
    """Returns the product of a and b."""
    return a * b

def divide_numbers(a, b):
    """Returns the quotient of a divided by b, or None if division by zero."""
    if b != 0:
        return a / b
    print("Cannot divide by zero")  
    return None

def modulo(a, b):
    """Returns the remainder when a is divided by b, or None if division by zero."""
    if b != 0:
        return a % b
    print("Cannot divide by zero")  
    return None

def euclid(a, b):
    """Returns the greatest common divisor (GCD) of a and b using Euclid's algorithm."""
    while b != 0:
        a, b = b, a % b
    return a

# Test values
A_VALUE = 5
B_VALUE = 3

SUM_RESULT = add(A_VALUE, B_VALUE)
print(f"The sum of a and b is {SUM_RESULT}")

DIFFERENCE = subtract(A_VALUE, B_VALUE)
print(f"The difference between a and b is {DIFFERENCE}")

PRODUCT = multiply(A_VALUE, B_VALUE)
print(f"The product of a and b is {PRODUCT}")

B_VALUE = 0
QUOTIENT = divide_numbers(A_VALUE, B_VALUE)
if QUOTIENT is not None:
    print(f"The quotient of a divided by b is {QUOTIENT}")

REMAINDER = modulo(A_VALUE, B_VALUE)
if REMAINDER is not None:
    print(f"The remainder when a is divided by b is {REMAINDER}")

GCD = euclid(A_VALUE, B_VALUE)
print(f"The GCD of a and b is {GCD}")
