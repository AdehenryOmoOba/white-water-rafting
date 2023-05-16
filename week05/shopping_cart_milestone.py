print()
print("Welcome to the Shopping Cart Program 🛒")

line = "--------------------------------------------------------------------------"

menu_list = ["add item", "view cart", "remove item", "compute total", "quit"]
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
            if menu_list[action_index] == "add item":
                print()
                item_name = input("What item would you like to add? ")
                item_list.append(item_name.capitalize())
                print()
                print(f"Success:'{item_name}' has been added to the cart ✔️")
            if menu_list[action_index] == "view cart":
                print()
                print("The contents of your shopping cart are:")
                print()
                for item in item_list:
                    print("-", item)
        else:
            print()
            print("❌ Error: You have selected an invalid action")
    except:
        print()
        print("❌ Error: Invalid option")    