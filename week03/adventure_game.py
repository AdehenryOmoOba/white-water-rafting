# In this challenge, i created a summary of the player's choices from the begining to the end of the game.

print()
print("Welcome to your game console 🎮")

line = "--------------------------------------------------------------------------"

print(line)

area_of_interest = input("Select your area of interest: \n1 - MATH\n2 - ENGLISH\n3 - GENERAL\n>>> ")

if area_of_interest.lower() in("math", "english", "general"):
    print(area_of_interest.capitalize() ,"is a great choice 👍")
    # --------------- Mathematics 
    if area_of_interest.lower() == "math":
        topic = input("which topic do you prefer? \n1 - PERMUTATION\n2 - ALGEBRA\n3 - GEOMETRY\n>>> ")
        if topic.lower() in("permutation", "algebra", "geometry"):
            difficulty_level = input("Select difficulty level: \n1 - EASY\n2 - MEDIUM\n>>> ")
            if topic.lower() in("permutation", "algebra", "geometry") and difficulty_level.lower() in("easy", "medium"):
                print(f"Here's your {difficulty_level.lower()} level {area_of_interest.lower()} ({topic.lower()}) question: ")
            if topic.lower() == "permutation" and difficulty_level.lower() == "easy":
                answer = input("Using all the letters of the word 'HYMN' how many distinct words can be formed ? \n>>> ")
                if answer == "24":
                    print("Correct answer, great job ✅")
                else:
                    print("Incorrect answer ❌, try again, you can do it!")
            elif topic.lower() == "permutation" and difficulty_level.lower() == "medium":
                answer = input("How many words can be formed (Without Repetition) with the letters of the word 'POSTMAN', if every word begins with P and ends with N ? \n>>> ")
                if answer == "120":
                    print("Correct answer, great job ✅")
                else:
                    print("Incorrect answer ❌, try again, you can do it!")
            elif topic.lower() == "algebra" and difficulty_level.lower() == "easy":
                answer = input("What is the value of 'x' in this expression: 5x + 25 = 70 ? \n>>> ")
                if answer == "9":
                    print("Correct answer, great job ✅")
                else:
                    print("Incorrect answer ❌, try again, you can do it!")
            elif topic.lower() == "algebra" and difficulty_level.lower() == "medium":
                answer = input("If 'y' = 6, what is the value of 'x' in this expression 9y ➗ 2x = 27 ? \n>>> ")
                if answer == "1":
                    print("Correct answer, great job ✅")
                else:
                    print("Incorrect answer ❌, try again, you can do it!")
            elif topic.lower() == "geometry" and difficulty_level.lower() == "easy":
                answer = input("A square has how many equal sides ? \n>>> ")
                if answer == "4":
                    print("Correct answer, great job ✅")
                else:
                    print("Incorrect answer ❌, try again, you can do it!")
            elif topic.lower() == "geometry" and difficulty_level.lower() == "medium":
                answer = input("A nonagon has how many sides ? \n>>> ")
                if answer == "9":
                    print("Correct answer, great job ✅")
                else:
                    print("Incorrect answer ❌, try again, you can do it!")
            else:
                print("You picked an invalid option, re-start the game.")
        else:
            print("You picked an invalid option, re-start the game.")
    # -------------- English
    elif area_of_interest.lower() == "english":
        topic = input("which topic do you prefer? \n1 - VOWELS\n2 - SYNONYMS\n>>> ")
        if topic.lower() in("vowels", "synonyms"):
            difficulty_level = input("Select difficulty level: \n1 - EASY\n2 - MEDIUM\n>>> ")
            if topic.lower() in("vowels", "synonyms") and difficulty_level.lower() in("easy", "medium"):
                print(f"Here's your {difficulty_level.lower()} level {area_of_interest.lower()} ({topic.lower()}) question: ")
            if topic.lower() == "vowels" and difficulty_level.lower() == "easy":
                answer = input("Name a word that starts with a vowel letter \n>>> ")
                if answer[0].lower() in("a","e","i","o","u"):
                    print("Correct answer, great job ✅")
                else:
                    print("Incorrect answer ❌, try again, you can do it!")
            elif topic.lower() == "vowels" and difficulty_level.lower() == "medium":
                answer = input("Answer 'true' or 'false'. Is the word 'union' a vowel sound? \n>>> ")
                if answer.lower() == "false":
                    print("Correct answer, great job ✅")
                else:
                    print("Incorrect answer ❌, try again, you can do it!")
            elif topic.lower() == "synonyms" and difficulty_level.lower() == "easy":
                answer = input("What is the synonym of 'ask' ? \n>>> ")
                if answer.lower() in("question", "inquire", "query"):
                    print("Correct answer, great job ✅")
                else:
                    print("Incorrect answer ❌, try again, you can do it!")
            elif topic.lower() == "synonyms" and difficulty_level.lower() == "medium":
                answer = input("What is the synonym of 'eager' ? \n>>> ")
                if answer.lower() in("keen", "fervent", "enthusiastic", "involved"):
                    print("Correct answer, great job ✅")
                else:
                    print("Incorrect answer ❌, try again, you can do it!")
            else:
                print("You picked an invalid option, re-start the game.")
        else:
            print("You picked an invalid option, re-start the game.")
    # ------------- General Knowledge
    else:
        topic = input("which topic do you prefer? \n1 - GEOGRAPHY\n2 - COMPUTER\n>>> ")
        if topic.lower() in("geography", "computer"):
            difficulty_level = input("Select difficulty level: \n1 - EASY\n2 - MEDIUM\n>>> ")
            if topic.lower() in("geography", "computer") and difficulty_level.lower() in("easy", "medium"):
                print(f"Here's your {difficulty_level.lower()} level {area_of_interest.lower()} knowledge ({topic.lower()}) question: ")
            if topic.lower() == "geography" and difficulty_level.lower() == "easy":
                answer = input("What is the diameter of the earth in kilometers (round to nearest whole number without commas) ? \n>>> ")
                if answer == "12742":
                    print("Correct answer, great job ✅")
                else:
                    print("Incorrect answer ❌, try again, you can do it!")
            elif topic.lower() == "geography" and difficulty_level.lower() == "medium":
                answer = input("How many continents are on earth ? \n>>> ")
                if answer == "7":
                    print("Correct answer, great job ✅")
                else:
                    print("Incorrect answer ❌, try again, you can do it!")
            elif topic.lower() == "computer" and difficulty_level.lower() == "easy":
                answer = input("How many bits is needed to store a single letter of the English alphabet using the ASCII encoding ? \n>>> ")
                if answer == "8":
                    print("Correct answer, great job ✅")
                else:
                    print("Incorrect answer ❌, try again, you can do it!")
            elif topic.lower() == "computer" and difficulty_level.lower() == "medium":
                answer = input("What is the meaning of the word “bit” ? \n>>> ")
                if answer.lower() == "binary digit":
                    print("Correct answer, great job ✅")
                else:
                    print("Incorrect answer ❌, try again, you can do it!")
            else:
                print("You picked an invalid option, re-start the game.")
        else:
            print("You picked an invalid option, re-start the game.")
else:
    print(area_of_interest, "is not on the menu, re-start the game.")
print(line)
print(f"Choice summary: \nArea of Interest: {area_of_interest.upper()} \nTopic: {topic.upper()}\nDifficulty Level: {difficulty_level.upper()}" )
print(line)