import random
import string

def generate_code(length=6):
    characters = string.ascii_letters + string.digits  # A-Z, a-z, 0-9
    return ''.join(random.choices(characters, k=length))

# Example usage
print(generate_code())
