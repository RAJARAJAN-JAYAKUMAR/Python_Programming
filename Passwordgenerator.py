import random
import string

def generate_password(length=12):
    # Define character sets for different types of characters
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine character sets
    all_characters = uppercase_letters + lowercase_letters + digits + special_characters

    # Ensure that the password length is at least 8
    length = max(length, 8)

    # Use random.choices to select characters with replacement
    password = ''.join(random.choices(all_characters, k=length))

    return password

# Example usage:
password = generate_password(length=16)
print("Generated Password:", password)
