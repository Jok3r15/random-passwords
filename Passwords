import random
import string


def generate_password(length=12):
    # Define the characters that can be used in the password
    all_characters = string.ascii_letters + string.digits + string.punctuation

    # Randomly select characters to form a password
    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password


# Example usage
password = generate_password(16)
print(f"Generated password: {password}")
