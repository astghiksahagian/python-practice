# Strings are really handy, so in this exercise you will learn how to make strings that have variables embedded in them. You embed variables inside a string by using a special {} sequence and then put the variable you want inside the {} characters. You also must start the string with the letter f for ”format”, as in f"Hello {somevar}". This little f before the " (double-quote) and the {} characters tell Python 3, ”Hey, this string needs to be formatted. Put these variables in there.”

name = "Zed A. Shaw"
age = 35
inches_to_centimeters = 2.54
height = 74 * inches_to_centimeters
pounds_to_kilograms = 0.45
weight = 180 * 0.45
eyes = "Blue"
teeth = "White"
hair = "Brown"

print(f"Let's talk about {name}.")
print(f"He's {height} centimeters tall")
print(f"He's {weight} kilograms heavy.")
print("Actually that's not that heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}")



