import random
import string

def generate_password(length):
    if length < 4:  # Ensures minimum length for including all character types
        print("Your password needs to have at least 4 characters.")
        return None

    # Character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # At least one character from each set
    all_characters = lower + upper + digits + symbols

    # Ensure password has at least one character from each category
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the rest of the password length with random choices
    password += random.choices(all_characters, k=length - 4)

    # Shuffle to avoid predictable patterns
    random.shuffle(password)

    # Join the list into a string
    return ''.join(password)

def main():
    print("Hi there! Let's make a strong and unique password just for you !")
    try:
        length = int(input("Enter the number of characters you want in your password (minimum 4): "))
        password = generate_password(length)
        if password:
            print(f"Success! Your new password is: {password}")
    except ValueError:
        print("Oops! That doesn't look like a number. Try again.")

if __name__ == "__main__":
    main()
