tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line\n{}.".format("and here's the rest of the sentece")
backslash_cat = "I'm \\ a \\ {}."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat.format("cat"))
print(fat_cat)

