# Combine everything you've learned.
# Ask user for a number, check if it's even, calculate its square root,
# and print a random motivational quote if the number is > 10.

# 💡 TIP:
# Combine `if`, `math`, `random`, and type conversion.

import math
import random   
quotes = [
    "Believe you can and you're halfway there.",
    "Your limitation—it's only your imagination.",
    "Push yourself, because no one else is going to do it for you.",
    "Great things never come from comfort zones.",
    "Dream it. Wish it. Do it."
]
user_input = input("Enter a number: ")
try:        
    number = float(user_input)
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")
    
    if number >= 0:
        sqrt_value = math.sqrt(number)
        print(f"The square root of {number} is {sqrt_value}.")
    else:
        print("Cannot compute the square root of a negative number.")
    
    if number > 10:
        quote = random.choice(quotes)
        print(f"Motivational Quote: {quote}")
except ValueError:
    print("Please enter a valid number.")
