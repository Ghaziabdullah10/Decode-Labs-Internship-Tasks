"""
Project 3: Random Password Generator
DecodeLabs - Python Programming Industrial Training Kit
"""

import string
import secrets


def get_password_length():
    """
    Ask the user for a password length and validate it.
    """
    while True:
        raw_value = input("Enter desired password length (min 8, max 64): ").strip()

        if not raw_value.isdigit():
            print("Invalid input. Please enter a whole number.\n")
            continue

        length = int(raw_value)
        if length < 8:
            print("Length too short. Please choose at least 8 characters.\n")
            continue
        if length > 64:
            print("Length too long. Please choose 64 characters or fewer.\n")
            continue

        return length


def get_character_pool(use_symbols=True):

    pool = string.ascii_letters + string.digits  # a-z, A-Z, 0-9
    if use_symbols:
        pool += string.punctuation
    return pool


def generate_password(length, use_symbols=True):

    pool = get_character_pool(use_symbols)

    # Guarantee complexity: pick one from each required category first.
    required_chars = [
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.digits),
    ]
    if use_symbols:
        required_chars.append(secrets.choice(string.punctuation))

    # Fill the rest of the password length from the full pool.
    remaining_length = length - len(required_chars)
    remaining_chars = [secrets.choice(pool) for _ in range(remaining_length)]

    all_chars = required_chars + remaining_chars

    for i in range(len(all_chars) - 1, 0, -1):
        j = secrets.randbelow(i + 1)
        all_chars[i], all_chars[j] = all_chars[j], all_chars[i]

    return "".join(all_chars)


def calculate_entropy(length, pool_size):

    import math
    return length * math.log2(pool_size)


def main():
    print("=== DecodeLabs Random Password Generator ===\n")

    length = get_password_length()

    symbols_choice = input("Include special symbols? (y/n): ").strip().lower()
    use_symbols = symbols_choice == "y"

    password = generate_password(length, use_symbols)
    pool_size = len(get_character_pool(use_symbols))
    entropy = calculate_entropy(length, pool_size)

    print("\nGenerated Password:")
    print(password)
    print(f"\nEstimated entropy: {entropy:.1f} bits")


if __name__ == "__main__":
    main()
