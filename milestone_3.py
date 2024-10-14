import random

# Step 1: Create a tuple of words to choose from
word_list = ('Banana', 'Orange', 'Watermelon', 'Strawberry', 'Pineapple')
# Randomly select a word from the list
secret_word = random.choice(word_list)

# Step 2: Define the check_guess function
def check_guess(guess):
    # Step 3: Convert the guess to lowercase
    guess = guess.lower()
    
    # Step 4: Check if the guess is in the secret word
    if guess in secret_word.lower():  # Convert secret_word to lowercase for comparison
        print(f"Good guess! '{guess}' is in the word.")
    else:
        print(f"Sorry, '{guess}' is not in the word. Try again.")

# Step 5: Define the ask_for_input function
def ask_for_input():
    while True:  # Step 1: Continuous loop
        # Step 2: Ask the user to guess a letter
        guess = input("Please guess a letter: ")
        
        # Step 3: Check if the guess is a single alphabetical character
        if len(guess) == 1 and guess.isalpha():
            # Step 4: Valid guess, break out of the loop
            break
        else:
            # Step 5: Invalid guess message
            print("Invalid letter. Please, enter a single alphabetical character.")
    
    # After breaking the loop, check if the guess is in the word
    check_guess(guess)

# Step 6: Call the ask_for_input function to start the game
ask_for_input()


