import random

def number_guessing_game():
    """A simple number guessing game."""
    secret_number = random.randint(1, 100)
    attempts = 0
    
    print("Guess the number between 1 and 100!")
    
    while True:
        guess = int(input("Your guess: "))
        attempts += 1
        
        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"Correct! You took {attempts} attempts.")
            break

if __name__ == "__main__":
    number_guessing_game()
