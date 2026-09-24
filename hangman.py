# THE HANGMAN GAME...

import random as r

words = {
    "python": "Programming",
    "html": "Web Development",
    "hangman": "Game",
    "computer": "Technology",
    "developer": "Career",
    "bee": "Insects",
    "butterfly": "Insects",
    "lion": "Animals",
    "tiger": "Animals",
}

incorrect_guesses = 0

selected_word = r.choice(list(words.keys()))

category = words[selected_word]

guessed_letters = []
guesses = []

print()
print("=" * 36)
print("|| Welcome to the Hangman Game!🎮 ||")
print("=" * 36)
print()

print("You have 6 incorrect guesses allowed.")
print(f"The category is: {category}")
print("Let's begin!")

for letter in selected_word:
    guessed_letters.append("_")
print(" ".join(guessed_letters))
print()

while incorrect_guesses < 6:
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    if guess in guesses:
        print("You already guessed that letter. Try again.")
        continue

    guesses.append(guess)

    if guess in selected_word:
        for i in range(len(selected_word)):
            if selected_word[i] == guess:
                guessed_letters[i] = guess
        print("Correct guess!")
        print(" ".join(guessed_letters))

    else:
        incorrect_guesses += 1
        print(
            f"Incorrect guess! You have {6 - incorrect_guesses}/6")

    if "_" not in guessed_letters:
        print("You successfully guessed the word!🥳")
        break


if incorrect_guesses == 6:
    print(f"You lost! The word was {selected_word}")

    print("Better luck next time! 😅")
