
Colour_to_hex = {"blue": "#0000ff", "cerise": "#de3163", "chestnut": "#954535", "eggplant": "#614051",
                 "electric indigo": "#6f00ff", "purple": "#a020f0", "rose": "#ff007f", "violet": "#ee82ee",
                 "Turquoise": "#40e0d0", "orchid": "#da70d6", "olive": "#808000"}

colour_name = input("Enter name of colour: ").lower()
while colour_name != "":
    if colour_name in Colour_to_hex:
        print(f"{colour_name}'s hex code is {Colour_to_hex[colour_name]}")
        colour_name = input("Enter name of colour: ").lower()
    else:
        print("Invalid colour name")
        colour_name = input("Enter name of colour: ").lower()
