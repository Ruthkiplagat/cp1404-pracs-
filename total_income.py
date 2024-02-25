def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    num_of_months = int(input("How many months? "))  # Refactored variable name

    for month in range(1, num_of_months + 1):
        income = float(input(f"Enter income for month {month}: "))  # Using f-string for input prompt
        incomes.append(income)

    print_report(num_of_months, incomes)


def print_report(num_of_months, incomes):
    """Prints the income report."""
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, num_of_months + 1):
        income = incomes[month - 1]
        total += income
        print(f"Month {month:2} - Income: ${income:10.2f} Total: ${total:10.2f}")


if __name__ == "__main__":
    main()