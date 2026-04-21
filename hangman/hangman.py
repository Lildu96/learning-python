import random

films = ["The Shawshank Redemption"] 
         # "The Godfather", "The Dark Knight", "The Lord Of The Rings", "Pulp Fiction"]

hangman_art = [
    r'''
    +-----+
    O     |
   /|\    |
   / \    |
      ====+'''

]
# Randomly choose a word
chosen_film = random.choice(films)

# Display "_" for each letter
film_display = []
for char in chosen_film:
    if char == " ":
        film_display.append(" ")
    else:
        film_display.append("_")

guessed_letters = []

attempts = 9

print("Welcome to Hangman!\n", hangman_art[0])
print("\nIn this game you will be guessing a film!")
input("Press Enter to start...")

while attempts > 0 and '_' in film_display:
    print("\n" + " ".join(film_display))
    guess = input("\nGuess a letter: ")

    if guess in chosen_film and guess not in guessed_letters:
        guessed_letters.append(guess)
        for index, letter in enumerate(chosen_film):
            if letter.casefold() == guess.casefold():
                film_display[index] = letter #reveal the letter
    else:
        print(hangman_art[0])
        attempts -= 1

    print("\nYour guessed letters are: " + " ".join(guessed_letters).upper())
    print(f"Attempts: {attempts}")

# Game conclusion
if "_" not in film_display:
    print("Congratulations, you guessed the film!")
    print(" ".join(film_display))
    print(hangman_art[0])
else:
    print("You Died!", hangman_art[0])