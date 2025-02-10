import argparse
import random
import string

def generate_password(length):
    # Define the characters that can be used in the password
    all_characters = string.ascii_letters + string.digits + string.punctuation

    # Randomly select characters to form a password
    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a secure random password.")
    parser.add_argument("--length", type=int, help="Length of the password")

    args = parser.parse_args()

    # If the length argument is not provided, ask the user to input it
    if args.length is None:
        length = int(input("Please enter the desired password length: "))
    else:
        length = args.length

    password = generate_password(length)
    print(f"Generated password: {password}")

# Example execution
# python "C:\Users\Gabriel_Gomez3\PycharmProjects\API Request to Gitlab\main.py" --length 16
