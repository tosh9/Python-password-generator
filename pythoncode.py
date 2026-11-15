import secrets
import string
import math

# Character sets
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
numbers = string.digits
special = "@#$%&*"

def generate_password(length, case_type):

    if length < 8:
        return "Password length must be at least 8!"

    # Select letter type
    if case_type == "lower":
        letters = lowercase
    elif case_type == "upper":
        letters = uppercase
    elif case_type == "mixed":
        letters = lowercase + uppercase
    else:
        return "Invalid character type!"

    # 50-30-20 distribution
    alpha_len = length // 2
    num_len = math.ceil(length * 0.30)
    special_len = length - alpha_len - num_len

    # Generate password characters
    password = (
        [secrets.choice(letters) for _ in range(alpha_len)] +
        [secrets.choice(numbers) for _ in range(num_len)] +
        [secrets.choice(special) for _ in range(special_len)]
    )

    # Securely shuffle characters
    secrets.SystemRandom().shuffle(password)

    return ''.join(password)


# Main program
print("--PASSWORD GENERATOR--")

length = int(input("Enter password length: "))

print("\n1. Lowercase")
print("2. Uppercase")
print("3. Mixed case")

choice = input("Choose character type (1/2/3): ")

types = {
    "1": "lower",
    "2": "upper",
    "3": "mixed"
}

password = generate_password(length, types.get(choice))

print("\nGenerated Password:", password)
