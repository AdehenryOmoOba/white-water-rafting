
# start
# Create a menu_list containing the options: "add item", "view cart", "remove item", "compute total", and "quit".
# Create empty item_list and price_list to store the items and prices in the shopping cart.
# Enter a loop that continues indefinitely.
#     Iterate over the menu_list and display each option with a corresponding number.
#     Display a prompt to select an action.
#     Try:

#         Read the user's input and store in a variable "action_index".
#         Subtract 1 from the action_index to align with the menu_list indices.
#         IF: Check if the action_index is within the valid range of menu_list indices.

#             If the action_index corresponds to "quit":
#                 Display a goodbye message.
#                 Display the line separator.
#                 Exit the loop.
#             If the action_index corresponds to "add item":
#                 Display a prompt to enter the item name.
#                 Read the user's input as item_name.
#                 Display a prompt to enter the item price.
#                 Read the user's input as item_price and convert it to a floating-point number.
#                 Format the item_price to two decimal places.
#                 Append item_name to item_list and item_price to price_list.
#                 Display a success message confirming the item addition.
#             If the action_index corresponds to "view cart":
#                 If item_list is empty:
#                     Display a message indicating that the cart is empty.
#                 Else:
#                     Display the contents of the shopping cart, showing each item and its price.
#             If the action_index corresponds to "compute total":
#                 Calculate the total price of all items in the shopping cart.
#                 Format the total price to two decimal places.
#                 Display the total price of the items in the shopping cart.
#             If the action_index corresponds to "remove item":
#                 Display a prompt to enter the index of the item to remove.
#                 Read the user's input as item_index and subtract 1 to align with list indices.
#                 Check if the item_index is within the valid range of item_list indices.
#                 If valid, remove the item and its price from item_list and price_list respectively.
#                 Display a message confirming the removal of the item.

#         Else: If the action_index is invalid:
#             Display an error message indicating that an invalid item number was selected.

#     Except:
#         Display an error message indicating an invalid option was chosen.
# End of the loop.
# End