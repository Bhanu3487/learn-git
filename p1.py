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
a_value = 5
b_value = 3

sum_result = add(a_value, b_value)
print(f"The sum of a and b is {sum_result}")

difference = subtract(a_value, b_value)
print(f"The difference between a and b is {difference}")

product = multiply(a_value, b_value)
print(f"The product of a and b is {product}")

b_value = 0
quotient = divide_numbers(a_value, b_value)
if quotient is not None:
    print(f"The quotient of a divided by b is {quotient}")

remainder = modulo(a_value, b_value)
if remainder is not None:
    print(f"The remainder when a is divided by b is {remainder}")

gcd = euclid(a_value, b_value)
print(f"The GCD of a and b is {gcd}")
