import random
import string

def generate_password(length=12):
    """Generate a random strong password."""
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

if __name__ == "__main__":
    length = int(input("Enter password length (default 12): ") or 12)
    password = generate_password(length)
    print(f"Generated Password: {password}")
