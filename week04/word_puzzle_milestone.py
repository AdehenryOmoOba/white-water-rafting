print()
print("Welcome to your game console 🎮")

line = "--------------------------------------------------------------------------"
print(line)

secret_word = "mathew"
guess_count = 0

while True:
    print()
    guess_word = input("What is your guess? ")
    if guess_word.lower() == secret_word:
        guess_count += 1
        print()
        print("✅ Congratulations! You guessed it 👍")
        print()
        print(f"It took you {guess_count} guess(es).")
        break
    else:
        guess_count += 1 
        print()
        print("❌ Your guess was not correct.")
print(line)