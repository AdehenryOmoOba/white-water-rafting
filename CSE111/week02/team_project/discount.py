import datetime


def get_day():
    today = datetime.date.today()
    return today.strftime("%A")


def calculate_discount(subtotal):
    day_name = get_day()
    if (day_name == "Tuesday" or day_name == "Wednesday") and subtotal >= 50:
        discount = subtotal * 0.10
        return discount
    else:
        return 0.00


def main():
    # Loop to get the subtotal
    subtotal = 0.00
    while True:
        price = input("Enter the price (enter 0 to finish): $")
        if price == "0":
            break
        quantity = int(input("Enter the quantity: "))
        subtotal = subtotal + float(price) * quantity

    discount = calculate_discount(subtotal)
    sales_tax = subtotal * 0.06
    total_amount_due = subtotal + sales_tax - discount

    if discount > 0:
        print(f"Discount: ${discount:.2f}")

    if get_day() in ["Tuesday", "Wednesday"] and subtotal < 50:
        additional_amount_needed = 50 - subtotal
        print(
            f"Additional amount needed for discount: ${additional_amount_needed:.2f}")

    print(f"Sales Tax (6%): ${sales_tax:.2f}")
    print(f"Total Amount Due: ${total_amount_due:.2f}")


main()
