def calculate_discount(price: float, discount_percent: float) -> float:
    # Check if the discount is 20% or higher
    if discount_percent >= 20:
        return price * (1 - discount_percent / 100)
    else:
        return price

def main():
    try:
        # Get user input for the original price
        original_price_str = input("Please enter the original price of the item: ")
        original_price = float(original_price_str)

        # Get user input for the discount percentage
        discount_percent_str = input("Please enter the discount percentage: ")
        discount_percent = float(discount_percent_str)

        # Call the function to calculate the final price
        final_price = calculate_discount(original_price, discount_percent)

        # Print the result based on whether a discount was applied
        if final_price != original_price:
            print(f"\nThe final price after the {discount_percent}% discount is: ${final_price:.2f}")
        else:
            print(f"\nNo discount was applied. The original price is: ${original_price:.2f}")

    except ValueError:
        print("Invalid input. Please enter a valid number for both the price and discount.")

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
