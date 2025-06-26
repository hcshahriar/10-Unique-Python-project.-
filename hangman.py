import random

WORDS = ["python", "hangman", "programming", "computer", "keyboard"]

def hangman():
    """Play a game of Hangman."""
    word = random.choice(WORDS)
    guessed = ["_"] * len(word)
    attempts = 6
    
    print("Welcome to Hangman!")
    print(" ".join(guessed))
    
    while attempts > 0 and "_" in guessed:
        guess = input("Guess a letter: ").lower()
        
        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed[i] = guess
            print(" ".join(guessed))
        else:
            attempts -= 1
            print(f"Wrong! {attempts} attempts left.")
    
    if "_" not in guessed:
        print("You won!")
    else:
        print(f"You lost! The word was: {word}")

if __name__ == "__main__":
    hangman()
