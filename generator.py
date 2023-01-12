import random
import string

def generate_password(length):
    # Create a list of all possible characters for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Use the random module to select a random set of characters from the list
    password = ''.join(random.choice(characters) for i in range(length))
    return password
