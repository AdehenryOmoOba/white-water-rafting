# line = "----------------------------------------------------------"
# first_name = input("What is your first name? ")
# last_name = input("What is your last name? ")
# email_address = input("What is your email address? ")
# phone_number = input("What is your phone number? ")
# job_title = input("What is your job title? ")
# id_number = input("What is your id number? ")
# print()
# print(
#     f"The ID Card is:\n{line}\n{last_name.upper()}, {first_name.capitalize()}\n{job_title.title()}\nID: {id_number}\n\n{email_address.lower()}\n{phone_number}\n{line}")


# Stretch Excercise
# line = "----------------------------------------------------------"
# first_name = input("What is your first name? ")
# last_name = input("What is your last name? ")
# email_address = input("What is your email address? ")
# phone_number = input("What is your phone number? ")
# job_title = input("What is your job title? ")
# id_number = input("What is your id number? ")

# hair_color = input("What is your hair color? ")
# eye_color = input("What is your eye color? ")
# month = input("What is your starting Month? ")
# training = input("Have you completed additional training? ")

# print()
# print(
#     f"The ID Card is:\n{line}\n{last_name.upper()}, {first_name.capitalize()}\n{job_title.title()}\nID: {id_number}\n\n{email_address.lower()}\n{phone_number}\n\nHair: {hair_color.capitalize():15}Eyes: {eye_color.capitalize()}\nMonth: {month.capitalize():14}Training: {training.capitalize()}\n{line}")

# Clever Stories
# months = ["january", "february", "march", "april", "may", "june",
#           "july", "august", "september", "october", "november", "december"]

# print()
# print("Welcome, let's write some stories 😄")
# print()

# adjective = input("Enter an adjective: ")
# animal = input("Enter a name of an animal: ")
# verb_1 = input("Enter a verb: ")
# exclamation = input("Enter an exclamation: ")
# verb_2 = input("Enter a verb: ")
# verb_3 = input("Enter a verb: ")
# birth_month = input("Enter a birth_month: ")
# conceive_month = ""

# birth_month_index = months.index(birth_month.lower())
# conceive_month_index = birth_month_index - 9
# if (conceive_month_index < 0):
#     conceive_month_index = conceive_month_index + 12
# conceive_month = months[conceive_month_index]
# # print("conceive month ", months[conceive_month_index])
# # print("birth month ", birth_month)

# story = f"The other day, I was really in trouble. \nIt all started when I saw a very {adjective.lower()} {animal.lower()} {verb_1.lower()} down the hallway. \n\"{exclamation.capitalize()}!\" I yelled. \nBut all I could think to do was to {verb_2.lower()} over and over. \nMiraculously, that caused it to stop, \nbut not before it tried to {verb_3.lower()} right in front of my family.\nMy mother told me that a person born in the month of {birth_month.capitalize()}, \nwas conceived around the month of {conceive_month}."
# print()
# print(story)
# print()

# with open("./week06/books.txt") as books_of_mormon:
#     for book in books_of_mormon:
#         print(book.strip())

# shopping_cart = [
#     ["Chips", 2.99],
#     ["Bread", 2.50],
#     ["Milk", 3.19],
#     ["Ice Cream", 6.99],
#     ["Cheese", 5.99],
#     ["Candy bar", 0.99]
# ]

# most_expensive = shopping_cart[0]

# for item in enumerate(shopping_cart):
#     (index, shop_item) = item
#     if shop_item[1] > most_expensive[1]:
#         most_expensive = shop_item

# print(most_expensive)