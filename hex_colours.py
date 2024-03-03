"""
Hexadecimal Colour Lookup
Estimate: 30 minutes
Actual:   40 minutes
"""

# Dictionary of hexadecimal colour codes
COLORS = {
    "ALICEBLUE": "#F0F8FF",
    "ANTIQUEWHITE": "#FAEBD7",
    "AQUA": "#00FFFF",
    "AQUAMARINE": "#7FFFD4",
    "AZURE": "#F0FFFF",
    "BEIGE": "#F5F5DC",
    "BISQUE": "#FFE4C4",
    "BLACK": "#000000",
    "BLANCHEDALMOND": "#FFEBCD",
    "BLUE": "#0000FF"
}


def main():
    print("Hexadecimal Colour Lookup")
    print("Enter a colour name to get its hexadecimal code.")
    print("Enter a blank name to stop the loop.")

    while True:
        color_name = input("Enter a colour name: ").upper()

        if color_name == "":
            print("Stopping the loop.")
            break

        color_code = COLORS.get(color_name)
        if color_code:
            print(f"The hexadecimal code for {color_name} is {color_code}.")
        else:
            print("Invalid colour name. Please try again.")


if __name__ == "__main__":
    main()
