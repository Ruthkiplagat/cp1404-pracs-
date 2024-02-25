name = "Gibson L-5 CES"
year = 1922
cost = 16035.4

# Formatting the guitar information using f-string
print(f"{year} {name} for about ${cost:,.0f}!")

# Generating the right-aligned numbers using a for loop
for i in range(0, 201, 50):
    print(f"{i: >4}")