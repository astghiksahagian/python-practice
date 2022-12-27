formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))

print(formatter.format("one","two", "three", "four"))

print(formatter.format(True, False, False, True))

print(formatter.format(formatter, formatter, formatter, formatter))

print(formatter.format(
    "I will try",
    "my best to",
    "excel in python",
    "this year."
))