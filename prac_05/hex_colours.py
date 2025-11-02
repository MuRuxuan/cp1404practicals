COLOUR_HEX={
    "Absolute Zero":"#0048ba",
    "Acid Green":"b0bf1a",
    "AliceBlue":"#f0f8ff",
    "AntiqueWhite2":"#eedfcc",
    "Azure3":"	#c1cdcd",
    "Barn Red":"#7c0a02",
    "Bleu de France":"#318ce7"
}

print("Enter a colour name (or press Enter to quit):")
while True:
    colour_name = input().strip()
    if not colour_name:
        break

    formatted_colour = colour_name.title()
    hex_code = COLOUR_HEX.get(formatted_colour)
    if hex_code:
        print(f"The hex code for {formatted_colour} is {hex_code}")
    else:
        print(f"Colour '{colour_name}' not found.")

    print("Goodbye!")


