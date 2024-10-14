import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)  # Pick a random word from the list
        self.word_guessed = ['_'] * len(self.word)  # Create a list of underscores for the letters in the word
        self.num_letters = len(set(self.word))  # Count the unique letters in the word
        self.num_lives = num_lives  # Set the number of lives the player has
        self.word_list = word_list  # Store the list of words
        self.list_of_guesses = []  # List to keep track of guessed letters

    def check_guess(self, guess):
        guess = guess.lower()  # Convert the guess to lowercase
        if guess in self.word:  # Check if the guessed letter is in the word
            print(f"Good guess! {guess} is in the word.")
            for index, letter in enumerate(self.word):  # Loop through each letter in the word
                if letter == guess:  # If the letter matches the guess
                    self.word_guessed[index] = guess  # Replace the underscore with the guessed letter
            self.num_letters -= 1  # Reduce the count of unique letters left to guess
        else:
            self.num_lives -= 1  # Decrease the number of lives if the guess is wrong
            print(f"Sorry, {guess} is not in the word. You have {self.num_lives} lives left.")

    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ")  # Ask the user to guess a letter
            if len(guess) != 1 or not guess.isalpha():  # Validate the input
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:  # Check if the letter has already been guessed
                print("You already tried that letter!")
            else:
                self.list_of_guesses.append(guess)  # Add the guess to the list of guesses
                self.check_guess(guess)  # Check if the guess is correct
                break  # Exit the loop after processing the guess

def play_game(word_list):
    num_lives = 5  # Number of lives for the player
    game = Hangman(word_list, num_lives)  # Create an instance of the Hangman class

    while True:  # Main game loop
        if game.num_lives == 0:  # Check if the player has lost
            print("You lost!")
            break  # Exit the loop if the player has lost
        if game.num_letters > 0:  # Check if the game should continue
            game.ask_for_input()  # Get a guess from the user
        else:  # If there are no letters left to guess
            print("Congratulations! You won the game!")  # Player wins
            break  # Exit the loop if the player has won

# Main execution
if __name__ == "__main__":
    word_list = ['apple', 'banana', 'cherry', 'orange']  # List of words to guess from
    play_game(word_list)  # Start the game by calling play_game with the word list
