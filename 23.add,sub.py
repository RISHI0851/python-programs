def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
def to_uppercase(text):
    return text.upper()

def to_lowercase(text):
    return text.lower()
from utilities import math_utils, string_utils

# Using math_utils
a = 10
b = 5
print("Addition:", math_utils.add(a, b))
print("Subtraction:", math_utils.subtract(a, b))

# Using string_utils
text = "Hello World"
print("Uppercase:", string_utils.to_uppercase(text))
print("Lowercase:", string_utils.to_lowercase(text))
