def add(a, b):
    return a + b

def subtract(a, b):
    return a - b  

def multiply(a, b):
    return a * b

def divide_numbers(a, b):
    if b != 0:
        return a / b
    print("Cannot divide by zero")  
    return None
        
def divide_numbers2(a, b):
    if b != 0:
        return a % b
    print("Cannot divide by zero")  
    return None
        
def euclid(a, b):
    while b != 0:  
        a, b = b, a % b
    return a

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

remainder = divide_numbers2(a_value, b_value)
if remainder is not None:
    print(f"The remainder when a is divided by b is {remainder}")

gcd = euclid(a_value, b_value)
print(f"The GCD of a and b is {gcd}")
