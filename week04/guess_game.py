import random

print()
print("Welcome to your game console 🎮")

line = "--------------------------------------------------------------------------"

repeat_game = True

while repeat_game == True:
    
    print(line)
    random_number = random.randint(1, 100)
    guess_count = 0
    invalid_guess = False
    
    while True:
        print()
        try:
            guessed_number = int(input("Guess the number: "))
        except:
            print()
            print("❌ Invalid response: Please input a number")
            invalid_guess = True
            break
        if guessed_number == random_number:
            guess_count += 1
            print()
            print("Correct!, you guessed it 👍")
            break
        else:
            if guessed_number > random_number:
                guess_count += 1
                print()
                print("Your guess is too high 🤔")
            else:
                guess_count += 1
                print()
                print("Your guess is too low 😪")
    
    print()
    if invalid_guess == False:
        print(f"You got the right number after {guess_count} guess(es)")
    print(line)
    
    repeat_game = False
    
    repeat_option = input("Do you want to play again? \n1 - Yes \n2 - No \n>>> ")
    if repeat_option.lower() in("yes", "no", "1", "2"):
        if repeat_option.lower() == "yes" or repeat_option == "1":
            repeat_game = True
        else:
            print("Bye bye!")
    else:
        print("You selected an invalid option")