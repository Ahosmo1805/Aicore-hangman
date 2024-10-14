import random
word_list = ('Banana', 'Orange', 'Watermelon', 'Strawberry', 'Pineapple')
word = random.choice(word_list)
print(word)

guess =input("Enter a fruit of you choice:.")
if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")

print("The random fruit was:", word)
print("Your guess was:",guess)

