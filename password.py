import random
import string

def generate_password(length=12, include_uppercase=True, include_numbers=True, include_symbols=True):
    # Define character pools
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if include_uppercase else ''
    numbers = string.digits if include_numbers else ''
    symbols = string.punctuation if include_symbols else ''

    # Combine character pools
    all_characters = lower + upper + numbers + symbols

    if not all_characters:
        raise ValueError("No characters available to generate a password. Check your options!")

    # Ensure at least one character from each selected pool
    password = []
    if include_uppercase:
        password.append(random.choice(upper))
    if include_numbers:
        password.append(random.choice(numbers))
    if include_symbols:
        password.append(random.choice(symbols))

    # Fill the rest of the password length with random choices
    password += random.choices(all_characters, k=length - len(password))

    # Shuffle the password to avoid predictable patterns
    random.shuffle(password)

    return ''.join(password)

# Example usage
if __name__ == "__main__":
    length = int(input("Enter the desired password length: "))
    include_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == 'yes'
    include_numbers = input("Include numbers? (yes/no): ").strip().lower() == 'yes'
    include_symbols = input("Include symbols? (yes/no): ").strip().lower() == 'yes'

    password = generate_password(
        length=length,
        include_uppercase=include_uppercase,
        include_numbers=include_numbers,
        include_symbols=include_symbols
    )
    print(f"Generated password: {password}")
