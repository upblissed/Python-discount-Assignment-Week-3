def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    If discount is less than 20%, returns the original price.
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    else:
        return price


# Prompt user for inputs
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(original_price, discount_percent)

    print(f"Final price: {final_price}")
except ValueError:
    print("Invalid input. Please enter numeric values.")
