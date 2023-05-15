# Requirements

# Have menu system that repeats until the user chooses quit.
# Create a list that will store the names of the items in the shopping cart.
# Complete the option to add the name of the item to the list.
# Complete the option to display the names of the items in the list.

# ==================================================================================

# Start
# Create a list of menu
# Create a cart (list) to store items
# Start a loop
# Prompt user to select a menu
# Use user's input to decide the next step
    # If user's choice is "add item", prompt user to write item to add, add the item to cart, provide feedback and repeat loop.
    # If user's choice is "view cart", loop through the cart and display each item and repeat loop.
    # If user's choice is "quit", break the loop to end the program
# End

# ================================================================================================

print()
print("Welcome to the Shopping Cart Program 🛒")

line = "--------------------------------------------------------------------------"

menu_list = ["buy foodstuff", "buy drinks", "view order", "quit"]
item_list = []

print(line)

while True:
    print()
    print("Please select one of the following: ")
    print()
    
    for i in range(len(menu_list)):
        print(f"{i + 1}. {menu_list[i].capitalize()}")
    
    print()
    try:
        action_index = int(input("Please enter an action: "))
    
        action_index -= 1
        
        if action_index < len(menu_list):
            if menu_list[action_index] == "quit":
                print()
                print("Thank you. Goodbye 👋")
                print()
                print(line)
                break
            if menu_list[action_index] == "buy foodstuff":
                print()
                food = input("What foodstuff do you want to buy? ")
                item_list.append(food)
                print()
                print(f"Success:'{food}' has been added to your order ✔️")
            if menu_list[action_index] == "buy drinks":
                print()
                drink = input("What drink do you want to buy? ")
                item_list.append(drink)
                print()
                print(f"Success:'{drink}' has been added to your order ✔️")
            if menu_list[action_index] == "view order":
                print()
                print("Summary of your order is:")
                print()
                for item in item_list:
                    print("-", item)
        else:
            print()
            print("❌ Error: You have selected an invalid action")
    except:
        print()
        print("❌ Error: Invalid option")    