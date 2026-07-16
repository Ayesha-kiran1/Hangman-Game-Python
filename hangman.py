import random

# Game ASCII art for visual feedback
HANGMAN_PICS = [
    '''
      +---+
          |
          |
          |
         ===''', '''
      +---+
      O   |
          |
          |
         ===''', '''
      +---+
      O   |
      |   |
          |
         ===''', '''
      +---+
      O   |
     /|   |
          |
         ===''', '''
      +---+
      O   |
     /|\\  |
          |
         ===''', '''
      +---+
      O   |
     /|\\  |
     /    |
         ===''', '''
      +---+
      O   |
     /|\\  |
     / \\  |
         ==='''
]

# Word bank with corresponding hints
WORDS_WITH_HINTS = {
    "python": "A popular programming language named after a comedy group, not the snake.",
    "network": "A group of interconnected computers or systems.",
    "firewall": "A security system that monitors and controls incoming/outgoing network traffic.",
    "virtualization": "The process of creating a software-based representation of physical servers.",
    "database": "An organized collection of structured information or data."
}

def play_hangman():
    # Select a random word and get its hint
    word = random.choice(list(WORDS_WITH_HINTS.keys()))
    hint = WORDS_WITH_HINTS[word]
    
    guessed_letters = set()
    attempts_left = len(HANGMAN_PICS) - 1
    
    print("=" * 50)
    print("Welcome to Python Hangman!")
    print("=" * 50)
    print(f"Hint: {hint}\n")
    
    while attempts_left > 0:
        # Display current hangman state
        print(HANGMAN_PICS[len(HANGMAN_PICS) - 1 - attempts_left])
        
        # Display word progress
        display_word = [letter if letter in guessed_letters else "_" for letter in word]
        print("Word: " + " ".join(display_word))
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        print(f"Attempts remaining: {attempts_left}\n")
        
        # Check if user won
        if "_" not in display_word:
            print(f"🎉 Congratulations! You guessed the word: '{word.upper()}'!")
            break
            
        # Get and validate user input
        guess = input("Guess a letter: ").strip().lower()
        print("-" * 30)
        
        # Validation checks
        if len(guess) != 1:
            print("❌ Invalid input! Please enter exactly ONE letter.")
            continue
        if not guess.isalpha():
            print("❌ Invalid input! Please enter an ALPHABET only.")
            continue
        if guess in guessed_letters:
            print(f"⚠️ You already guessed '{guess}'. Try a different letter.")
            continue
            
        # Add to guessed list
        guessed_letters.add(guess)
        
        # Check if guess is correct
        if guess in word:
            print(f"✅ Good job! '{guess}' is in the word.")
        else:
            print(f"❌ Oops! '{guess}' is not in the word.")
            attempts_left -= 1
            
    else:
        # If loop finishes with attempts_left == 0 (User lost)
        print(HANGMAN_PICS[-1])
        print(f"💀 Game Over! The word was: '{word.upper()}'. Better luck next time!")

if __name__ == "__main__":
    play_hangman()