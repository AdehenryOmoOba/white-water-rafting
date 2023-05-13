# I added a birth month estimator, it estimates a person's birth month by subtracting nine months from their birth month.

months = ["january", "february", "march", "april", "may", "june",
          "july", "august", "september", "october", "november", "december"]

print()
print("Welcome, let's write some stories 😄")
print()

line = "--------------------------------------------------------------------------"
adjective = input("Enter an adjective: ")
animal = input("Enter a name of an animal: ")
verb_1 = input("Enter a verb: ")
exclamation = input("Enter an exclamation: ")
verb_2 = input("Enter a verb: ")
verb_3 = input("Enter a verb: ")
birth_month = input("Enter a birth_month: ")
conceive_month = ""

birth_month_index = months.index(birth_month.lower())
conceive_month_index = birth_month_index - 9
if (conceive_month_index < 0):
    conceive_month_index = conceive_month_index + 12
conceive_month = months[conceive_month_index]

story = f"{line}\nThe other day, I was really in trouble. \nIt all started when I saw a very {adjective.lower()} {animal.lower()} {verb_1.lower()} down the hallway. \n\"{exclamation.capitalize()}!\" I yelled. \nBut all I could think to do was to {verb_2.lower()} over and over. \nMiraculously, that caused it to stop, \nbut not before it tried to {verb_3.lower()} right in front of my family.\nMy mother told me that a person born in the month of {birth_month.capitalize()}, \nwas conceived around the month of {conceive_month.capitalize()}.\n{line}"
print()
print(story)
print()
