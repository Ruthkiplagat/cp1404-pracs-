# CP1404/CP5632 - Practical
# Answer the following questions:
# 1. When will a ValueError occur?
#    A ValueError will occur if the user enters a value that cannot be converted to an integer, such as a string.

# 2. When will a ZeroDivisionError occur?
#    A ZeroDivisionError will occur if the user enters 0 as the denominator, leading to division by zero.

# 3. Could you change the code to avoid the possibility of a ZeroDivisionError?
#    Yes, we can add a condition to check if the denominator is 0 before performing the division operation.

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    # Check if denominator is not 0 before performing division
    if denominator == 0:
        print("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")