import random

# Step 1: Create a Hangman class
class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list).lower()  # Select a random word and convert to lowercase
        self.word_guessed = ['_'] * len(self.word)  # Initialize the word guessed with underscores
        self.num_lives = num_lives  # Set the number of lives
        self.list_of_guesses = []  # Initialize an empty list for guesses

    def check_guess(self, guess):
        guess = guess.lower()  # Convert the guess to lowercase
        if guess in self.word:  # Check if the guess is correct
            print(f"Good guess! '{guess}' is in the word.")
            for index, letter in enumerate(self.word):
                if letter == guess:  # Replace underscores with the correct letter
                    self.word_guessed[index] = letter
            if '_' not in self.word_guessed:  # Check if the word is completely guessed
                print(f"Congrats! You have guessed the word: {self.word}!")
                return True  # End game
        else:
            self.num_lives -= 1  # Reduce lives if the guess is incorrect
            print(f"Sorry, '{guess}' is not in the word. You have {self.num_lives} lives left.")
            if self.num_lives == 0:
                print("Game over! You ran out of lives.")
                return True  # End game
        return False  # Continue game

    def ask_for_input(self):
        while True:
            guess = input("Please guess a letter: ")
            if len(guess) != 1 or not guess.isalpha():  # Check for valid input
                print("Invalid letter. Please enter a single alphabetical character.")
            elif guess in self.list_of_guesses:  # Check if the letter was already guessed
                print("You already tried that letter!")
            else:
                self.list_of_guesses.append(guess)  # Add the guess to the list
                if self.check_guess(guess):  # Check the guess and see if the game ends
                    break  # Exit if the game is over

# Create a list of words to guess from
word_list = ['apple', 'banana', 'cherry', 'orange']
hangman_game = Hangman(word_list)

# Start the game
print(f"Word to guess: {''.join(hangman_game.word_guessed)}")
while hangman_game.num_lives > 0:
    hangman_game.ask_for_input()  # Keep asking for input until the game ends

