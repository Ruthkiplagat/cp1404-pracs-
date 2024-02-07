# shop_calculator.py
# Shop Calculator

# Function to calculate total price with discount
def calculate_total_price(num_items, prices):
    total_price = sum(prices)
    if total_price > 100:
        total_price *= 0.9  # Apply 10% discount if total price is over $100
    return total_price

# Main program
def main():
    # Input validation loop for number of items
    while True:
        try:
            num_items = int(input("Number of items: "))
            if num_items < 0:
                raise ValueError("Invalid number of items!")
            break  # Exit the loop if input is valid
        except ValueError as ve:
            print(ve)

    prices = []
    for i in range(num_items):
        while True:
            try:
                price = float(input(f"Price of item {i + 1}: "))
                if price <= 0:
                    raise ValueError("Price must be greater than zero!")
                break  # Exit the loop if input is valid
            except ValueError as ve:
                print(ve)
        prices.append(price)

    total_price = calculate_total_price(num_items, prices)
    print(f"Total price for {num_items} items is ${total_price:.2f}")

if __name__ == "__main__":
    main()