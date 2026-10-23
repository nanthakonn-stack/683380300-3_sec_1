

import my_utils
import math
import random


# Use the custom module
my_utils.greet("Alice")

print("\nPrime Number Test")
print("Is 7 prime?", my_utils.is_prime(7))
print("Is 10 prime?", my_utils.is_prime(10))
print("Is 13 prime?", my_utils.is_prime(13))


# Use the math module
number = 25
result = math.sqrt(number)

print("\nSquare Root")
print("Square root of", number, "is", result)


# Use the random module
random_number = random.randint(1, 100)

print("\nRandom Number")
print("Random number between 1 and 100:", random_number)
