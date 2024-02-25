# Write user's name to a file
name = input("Enter your name: ")
with open("name.txt", 'w') as file:
    file.write(name)

# Read user's name from the file and print it
with open("name.txt", 'r') as file:
    name = file.read().strip()
print(f"Your name is {name}")

# Read first two numbers from numbers.txt and print their sum
with open("numbers.txt", 'r') as file:
    number1 = int(file.readline().strip())
    number2 = int(file.readline().strip())
    total = number1 + number2
print("Sum of first two numbers:", total)

# Calculate sum of all numbers in numbers.txt
total = 0
with open("numbers.txt", 'r') as file:
    for line in file:
        number = int(line.strip())
        total += number
print("Sum of all numbers:", total)