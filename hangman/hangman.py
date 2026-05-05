import random

films = ["The Shawshank Redemption",
          "The Godfather", "The Dark Knight", "The Lord Of The Rings", "Pulp Fiction"]

hangman_art = [
    r'''
    




    ''',
    r'''

    


      ====+
    ''',
    r'''
          +
          |
          |
          |
      ====+
    ''',
    r'''
    +-----+
          |
          |
          |
      ====+
    ''',
    r'''
    +-----+
    0     |
          |
          |
      ====+
    ''',
    r'''
    +-----+
    0     |
    |     |
          |
      ====+
    ''',
    r'''
    +-----+
    0     |
    |\    |
          |
      ====+
    ''',
    r'''
    +-----+
    0     |
   /|\    |
          |
      ====+
    ''',
    r'''
    +-----+
    0     |
   /|\    |
     \    |
      ====+
    ''',
    r'''
    +-----+
    O     |
   /|\    |
   / \    |
      ====+
    '''
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

print("Welcome to Hangman!\n", hangman_art[9])
print("\nIn this game you will be guessing a film!")
input("Press Enter to start...")

while attempts > 0 and '_' in film_display:

    print("\n" + " ".join(film_display))
    guess = input("\nGuess a letter or the film: ").casefold()

    if len(guess) == 1:

        # split answer into letter or film guess
        #if len(guess) == 1: #letter logic
        if guess in chosen_film.casefold() and guess not in guessed_letters:
                for index, letter in enumerate(chosen_film):
                    if letter.casefold() == guess:
                        film_display[index] = letter #reveal the letter
        else:
                attempts -= 1

        # Add new guess to guessed_letters
        if guess not in guessed_letters:
                guessed_letters.append(guess)
    # full title logic
    else:
        if guess == chosen_film.casefold():
             film_display = list(chosen_film)
        else:
            attempts -= 1


    art_stage = 9 - attempts

    print(hangman_art[art_stage])
    print("\nYour guessed letters are: " + " ".join(guessed_letters).upper())
        

# Game conclusion
if "_" not in film_display:
    print("Congratulations, you guessed the film!")
    print(" ".join(film_display))
    print(hangman_art[art_stage])
else:
    print("You Died!\n", hangman_art[9])