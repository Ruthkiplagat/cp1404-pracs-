is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True  # Set is_finished to True when a valid integer is entered
    except ValueError:  # Catch ValueError exception
        print("Please enter a valid integer.")
print("Valid result is:", result)