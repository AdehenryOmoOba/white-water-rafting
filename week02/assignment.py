# I added a functionality that gives the customer a complimentary bottle of coca-cola if their total spending (including tax) is above $20.
 
print()
print("Welcome to BYU restruant 😄")

line = "--------------------------------------------------------------------------"

print(line)

child_meal_price = float(input("What is the price of a child's meal? "))
adult_meal_price = float(input("What is the price of an adult's meal? "))
number_of_children = int(input("How many children are there? "))
number_of_adults = int(input("How many adults are there? "))
tax_rate = float(input("What is the sales tax rate? "))

subtotal = (child_meal_price * number_of_children) + (adult_meal_price * number_of_adults)
sales_tax = (tax_rate / 100) * subtotal
total = subtotal + sales_tax

print()

print("Subtotal:", "${:.2f}".format(subtotal))
print("Sales Tax:", "${:.2f}".format(sales_tax))
print("Total:", "${:.2f}".format(total))

print()

payment_amount = float(input("What is the payment amount? "))
change = payment_amount - total

print("Change:", "${:.2f}".format(change))

if (total > 20):
    print("Hurray!, you have a complimentary bottle of coca-cola for spending above $20")

print(line)