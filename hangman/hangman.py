import random

films = ["The Shawshank Redemption", "The Godfather", "The Dark Knight", "The Lord Of The Rings", "Pulp Fiction"]

hangman_art = [
    '''
    +-----+
    O     |
   /|\    |
   / \    |
      ====+'''

]
# Randomly choose a word
chosen_film = random.choice(films)

# Display "_" for each letter
film_display = ['_' for _ in chosen_film]
attempts = 9

print("Welcome to Hangman!\n", hangman_art[0])

while attempts > 0 and '_' in film_display:
    print("\n" + " ".join(film_display))
    guess = input("Guess a letter: ")
    if guess in chosen_film:
        for index, letter in enumerate(chosen_film):
            if letter == guess:
                film_display[index] = guess #reveal the letter
    else:
        print(hangman_art[0])
        attempts -= 1

# Game conclusion
if "_" not in film_display:
    print("Congratulations, you guessed the film!")
    print(" ".join(film_display))
    print(hangman_art[0])
else:
    print("You Died!", hangman_art[0])