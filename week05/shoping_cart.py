# I added an extra check to let the user know they have an empty cart if they try to check their cart without adding anything to the cart at first.

print()
print("Welcome to the Shopping Cart Program 🛒")

line = "--------------------------------------------------------------------------"

menu_list = ["add item", "view cart", "remove item", "compute total", "quit"]
item_list = []
price_list = []

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
            elif menu_list[action_index] == "add item":
                print()
                item_name = input("What item would you like to add? ")
                print()
                item_price = float(input(f"What is the price of {item_name} ? "))
                item_price = "{:.2f}".format(item_price)
                
                item_list.append(item_name)
                price_list.append(item_price)
                
                print()
                print(f"Success:'{item_name}' has been added to the cart ✔️")
            elif menu_list[action_index] == "view cart":
                if len(item_list) == 0:
                    print()
                    print("Your cart is currently empty, select option (1) to start shopping now!")
                else:
                    print()
                    print("The contents of your shopping cart are:")
                    print()
                    for i in range(len(item_list)):
                        item = item_list[i]
                        price = price_list[i]
                        print(f"{i + 1}. {item} - ${price}")
            elif menu_list[action_index] == "compute total":
                print()
                cart_total = 0
                for price in price_list:
                    cart_total += float(price)
                formatted_cart_total = "{:.2f}".format(cart_total)
                print(f"The total price of all items in the shopping cart is ${formatted_cart_total}")
            elif menu_list[action_index] == "remove item":
                print()
                item_index = int(input("Which item would you like to remove? "))
                item_index -= 1
                
                if 0 <= item_index < len(item_list):
                    removed_item = item_list.pop(item_index)
                    price_list.pop(item_index)
                    print()
                    print(f"'{removed_item}' has been removed from your cart!")
            else:
                print()
                print("Error: You have selected an invalid item number")
        else:
            print()
            print("❌ Error: You have selected an invalid action")
    except:
        print()    
        print("❌ Error: Invalid option")    