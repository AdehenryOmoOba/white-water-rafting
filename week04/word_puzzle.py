# I created a 'lifeline' variable to track the number of guesses the player is allowed to make.

import random

#  The screen is clear, audio is what ?

words_list = [
    "Nephi",
    "Grace",
    "Revelation",
    "Ammon",
    "Faith",
    "Isreal",
    "Moroni",
    "Love",
    "Penalty",
    "Alma",
    "Covenant",
    "Levi",
    "Lamanite",
    "Redemption",
    "Goalkeeper",
    "Jaredite",
    "Resurrection",
    "Three",
    "Zarahemla",
    "Salvation"
]

print()
print("Welcome to your game console 🎮")

line = "--------------------------------------------------------------------------"
print(line)

secret_word = words_list[random.randint(0, 20)].lower()
hint = ""
guess_count = 0
lifeline = 6

for letter in secret_word:
    hint += "_ "

print("Your hint is: ", hint)

while True:
    print()
    if lifeline == 0:
        print("Game over! You have used all your lifelines.")
        break
    guess_word = input("What is your guess? ")
    if guess_word.lower() == secret_word:
        guess_count += 1
        print()
        print("Congratulations! You guessed it 👍")
        print()
        print(f"It took you {guess_count} guess(es).")
        break
    if len(guess_word) != len(secret_word):
        guess_count += 1
        lifeline -= 1
        print()
        print("❌ Sorry, the guess word must have the same number of letters as the secret word.")
        print()
        print(f"You have {lifeline} lifeline left")
    else:
        guess_count += 1
        lifeline -= 1
        hint = ""
        for i,letter in enumerate(guess_word):
            if letter.lower() in(secret_word):
                if secret_word[i] == letter.lower():
                    hint += f"{letter.upper()} "
                else:
                    hint += f"{letter.lower()} "
            else:
                hint += "_ "
        if lifeline > 0:
            print()
            print("Your hint is: ", hint)
        print()    
        print(f"You have {lifeline} lifeline left")
print(line)